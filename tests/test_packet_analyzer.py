import unittest
from app.packet_analyzer import PacketAnalyzer
from app.database import Database

class MockPacket:
    def __init__(self, src_ip, dst_ip):
        self.src_ip = src_ip
        self.dst_ip = dst_ip

    def haslayer(self, layer):
        return True

    def __getitem__(self, key):
        class IP:
            def __init__(self, src, dst):
                self.src = src
                self.dst = dst
        return IP(self.src_ip, self.dst_ip)

class TestPacketAnalyzer(unittest.TestCase):
    def setUp(self):
        self.db = Database()
        self.analyzer = PacketAnalyzer(self.db)

    def test_analyze_packet(self):
        packet = MockPacket("192.168.1.1", "10.0.0.1")
        self.analyzer.analyze_packet(packet)
        self.assertEqual(self.analyzer.packet_count, 1)
        self.assertEqual(self.analyzer.ip_counter["192.168.1.1"], 1)
        self.assertEqual(self.analyzer.ip_counter["10.0.0.1"], 1)

    def test_dos_detection(self):
        for _ in range(101):
            packet = MockPacket("192.168.1.1", "10.0.0.1")
            self.analyzer.analyze_packet(packet)
        
        alerts = self.db.get_alerts()
        self.assertTrue(any("Potential DoS attack from 192.168.1.1" in alert[1] for alert in alerts))

if __name__ == '__main__':
    unittest.main()
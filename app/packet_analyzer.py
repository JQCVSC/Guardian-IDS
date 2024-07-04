import scapy.all as scapy
from collections import Counter

class PacketAnalyzer:
    def __init__(self, db):
        self.db = db
        self.packet_count = 0
        self.ip_counter = Counter()

    def start(self):
        scapy.sniff(prn=self.analyze_packet, store=False)

    def analyze_packet(self, packet):
        self.packet_count += 1
        if packet.haslayer(scapy.IP):
            ip_src = packet[scapy.IP].src
            ip_dst = packet[scapy.IP].dst
            self.ip_counter.update([ip_src, ip_dst])

            # Simple rule: Alert if a single IP sends more than 1000 packets
            if self.ip_counter[ip_src] > 1000:
                self.db.add_alert(f"Potential DoS attack from {ip_src}")

    def get_stats(self):
        return {
            "total_packets": self.packet_count,
            "top_ips": self.ip_counter.most_common(5)
        }
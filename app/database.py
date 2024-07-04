import sqlite3
from datetime import datetime

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('ids.db', check_same_thread=False)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS alerts
            (id INTEGER PRIMARY KEY, message TEXT, timestamp TEXT)
        ''')
        self.conn.commit()

    def add_alert(self, message):
        cursor = self.conn.cursor()
        timestamp = datetime.now().isoformat()
        cursor.execute('INSERT INTO alerts (message, timestamp) VALUES (?, ?)',
                       (message, timestamp))
        self.conn.commit()

    def get_alerts(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM alerts ORDER BY timestamp DESC LIMIT 10')
        return cursor.fetchall()
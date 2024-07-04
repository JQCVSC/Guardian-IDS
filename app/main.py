from flask import Flask, render_template
from packet_analyzer import PacketAnalyzer
from database import Database
import threading

app = Flask(__name__)
db = Database()
analyzer = PacketAnalyzer(db)

@app.route('/')
def index():
    alerts = db.get_alerts()
    stats = analyzer.get_stats()
    return render_template('index.html', alerts=alerts, stats=stats)

def start_analyzer():
    analyzer.start()

if __name__ == '__main__':
    threading.Thread(target=start_analyzer, daemon=True).start()
    app.run(host='0.0.0.0', port=8080)
    
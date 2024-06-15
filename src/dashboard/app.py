# src/dashboard/app.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template
import psutil
from defense.mitigation import get_mitigation_status

app = Flask(__name__)

def get_network_traffic():
    traffic_metrics = {}
    net_io = psutil.net_io_counters()

    traffic_metrics['packets_per_second'] = net_io.packets_sent + net_io.packets_recv
    traffic_metrics['server_load'] = psutil.cpu_percent(interval=1) / 100.0
    traffic_metrics['mitigation_actions'] = get_mitigation_status()

    return traffic_metrics

@app.route('/')
def home():
    traffic_metrics = get_network_traffic()
    return render_template('index.html', **traffic_metrics)

if __name__ == '__main__':
    app.run(debug=True)

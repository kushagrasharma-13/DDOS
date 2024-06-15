# src/dashboard/app.py
from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    traffic_metrics = {
        'packets_per_second': random.randint(10, 100),
        'server_load': random.uniform(0.1, 1.0),
        'mitigation_actions': 'No active actions'
    }
    return render_template('index.html', **traffic_metrics)

if __name__ == '__main__':
    app.run(debug=True)
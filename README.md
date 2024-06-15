# Defense Against DDoS Attacks

## Overview
This project aims to develop a defense framework to protect a server against Distributed Denial of Service (DDoS) attacks.

## Key Features
- Network Traffic Monitoring
- Defensive Measures
- User-Friendly Dashboard
- Alert System
- Automated IP Blacklisting
- DDoS Attack Simulation Tool
- Machine Learning for Attack Detection

## Setup
1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
2. Start the dashboard:
    ```sh
    cd src/dashboard
    FLASK_APP=app.py flask run
    ```

## Usage
- Run packet sniffer: `python src/monitoring/packet_sniffer.py`
- Compile Java DDoS tool: `sh compile.sh`
- Train machine learning model: `python src/machine_learning/train_model.py`
- Run tests: `pytest tests/`
# src/defense/mitigation.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
from defense.ip_blacklist import clear_expired_blacklists
from utils import logger

def start_defensive_measures():
    # Periodically clear expired blacklists
    while True:
        clear_expired_blacklists()
        time.sleep(60)

if __name__ == "__main__":
    start_defensive_measures()
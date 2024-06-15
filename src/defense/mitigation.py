# src/defense/mitigation.py

import sys
import os
import time
from defense.ip_blacklist import clear_expired_blacklists
from utils import logger

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

mitigation_status = "No active actions"

def start_defensive_measures():
    global mitigation_status
    while True:
        try:
            clear_expired_blacklists()
            mitigation_status = "Blacklist cleared at " + time.strftime("%Y-%m-%d %H:%M:%S")
        except Exception as e:
            mitigation_status = f"Error in clearing blacklist: {e}"
        time.sleep(60)

def get_mitigation_status():
    return mitigation_status

if __name__ == "__main__":
    start_defensive_measures()

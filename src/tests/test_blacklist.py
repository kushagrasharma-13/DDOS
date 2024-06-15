# src/tests/test_blacklisting.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from datetime import datetime, timedelta
from src.defense.ip_blacklist import blacklist_ip, clear_expired_blacklists, blacklisted_ips
import time

if __name__ == "__main__":
    test_ip = '192.168.1.100'
    print(f"Blacklisting IP: {test_ip}")
    blacklist_ip(test_ip)
    print(f"Blacklisted IPs: {blacklisted_ips}")

    print("Waiting for 2 minutes...")
    time.sleep(120)
    clear_expired_blacklists()
    print(f"Blacklisted IPs after clearing: {blacklisted_ips}")
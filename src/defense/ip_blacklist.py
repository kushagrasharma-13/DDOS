import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datetime import datetime, timedelta
BLACKLIST_DURATION_MINUTES = 30
from utils import logger

blacklisted_ips = {}

def blacklist_ip(ip):
    expiration_time = datetime.now() + timedelta(minutes=BLACKLIST_DURATION_MINUTES)
    os.system(f"netsh advfirewall firewall add rule name=\"block_{ip}\" dir=in action=block remoteip={ip}")
    blacklisted_ips[ip] = expiration_time
    logger.info(f"IP {ip} blacklisted until {expiration_time}")

def clear_expired_blacklists():
    current_time = datetime.now()
    expired_ips = [ip for ip, expiry in blacklisted_ips.items() if expiry < current_time]
    for ip in expired_ips:
        os.system(f"netsh advfirewall firewall delete rule name=\"block_{ip}\"")
        del blacklisted_ips[ip]
        logger.info(f"IP {ip} removed from blacklist")
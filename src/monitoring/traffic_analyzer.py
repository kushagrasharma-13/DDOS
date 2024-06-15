import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from collections import defaultdict
from threading import Thread, Lock
from scapy.layers.inet import IP
from src.utils import logger, send_alert
from src.config import ALERT_THRESHOLD_PACKETS_PER_SECOND, THRESHOLD_PACKETS_PER_SECOND
from src.defense.ip_blacklist import blacklist_ip
import time

packet_counts = defaultdict(int)
lock = Lock()

def reset_packet_counts():
    global packet_counts
    while True:
        time.sleep(1)
        with lock:
            packet_counts.clear()

def analyze_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        with lock:
            packet_counts[src_ip] += 1

            # Check for high packet rate from the same IP
            if packet_counts[src_ip] > ALERT_THRESHOLD_PACKETS_PER_SECOND:
                msg = f"Potential DDoS attack detected from IP: {src_ip}"
                send_alert(msg)
                logger.warning(msg)

                if packet_counts[src_ip] > THRESHOLD_PACKETS_PER_SECOND:
                    blacklist_ip(src_ip)
                    logger.warning(f"IP {src_ip} blacklisted due to excessive packets")

def start_traffic_analysis():
    reset_thread = Thread(target=reset_packet_counts)
    reset_thread.daemon = True
    reset_thread.start()

if __name__ == "__main__":
    start_traffic_analysis()
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scapy.all import sniff
ALERT_THRESHOLD_PACKETS_PER_SECOND = 30
from defense import ip_blacklist
from monitoring.traffic_analyzer import analyze_packet, start_traffic_analysis
from utils import logger, send_alert

def packet_callback(packet):
    analyze_packet(packet)

def start_sniffing():
    start_traffic_analysis()  # Start the traffic analysis thread
    sniff(iface='Wi-Fi', prn=packet_callback, store=0)

if __name__ == "__main__":
    start_sniffing()
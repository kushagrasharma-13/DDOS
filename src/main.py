from monitoring import packet_sniffer
from defense import ip_blacklist, mitigation
import time

def main():
    packet_sniffer.start_sniffing()
    mitigation.start_defensive_measures()

if __name__ == '__main__':
    main()
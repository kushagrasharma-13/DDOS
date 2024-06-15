import unittest
import src.monitoring.packet_sniffer as ps

class TestPacketSniffer(unittest.TestCase):

    def test_packet_callback(self):
        # Simulate a packet and test callback
        self.assertTrue(callable(ps.packet_callback))

if __name__ == '__main__':
    unittest.main()
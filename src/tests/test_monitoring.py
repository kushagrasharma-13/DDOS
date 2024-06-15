import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import monitoring.packet_sniffer as ps

class TestPacketSniffer(unittest.TestCase):

    def test_packet_callback(self):
        self.assertTrue(callable(ps.packet_callback))

if __name__ == '__main__':
    unittest.main()
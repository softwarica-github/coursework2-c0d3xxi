import unittest
from PortScanner import *


class TestPorts(unittest.TestCase):
    def setup(self):
        pass
        
    def teardown(self):
        pass
        
    def test_scanner(self):
        
        test_scanner=scan_res()
        self.assertEqual(self.scanner, test_scan)
           

if __name__=='__main__':
    unittest.main()

#!/usr/bin/env python3

import unittest

class TestTexInterface(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTempInBounds(self):
        self.assertGreater(30, 32,
                         'Temperature greater than 32 deg F')
        '''
        self.assertGreater(self.texInterface.getTemperature(), 32,
                         'Temperature greater than 32 deg F')
        self.assertLess   (self.texInterface.getTemperature(), 110.0,
                         'Temperature less than 110 deg F')
        '''

if __name__ == '__main__':
    unittest.main()

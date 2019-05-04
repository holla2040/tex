#!/usr/bin/env python3
import sys
import os

(filePath, fileName) = os.path.split(__file__)
sys.path.insert(0,os.path.join(filePath, ".."))

import unittest
from texInterface import TexInterface

class TestTexInterface(unittest.TestCase):
    def setUp(self):
        self.texInterface = TexInterface()
        
    def msgToScreenGetResponse(self, message):
        
    def tearDown(self):
        pass

    def testTempFInBounds(self):
        temp = self.texInterface.getTempF()
        self.assertGreater(temp, 32,
                         'Temperature greater than 32 deg F')
        self.assertLess   (temp, 110.0,
                         'Temperature less than 110 deg F')
        
    def testTempCInBounds(self):
        temp = self.texInterface.getTempC()
        self.assertGreater(temp, 0,
                         'Temperature greater than 0 deg C')
        self.assertLess   (temp, 43.0,
                         'Temperature less than 43 deg C')
    def testTempFViaHuman(self):
        temp = self.texTinterface.getTempF()
        #Write question out to screen
        #Get response                        yes    no
        #If response is no, fail the test    \/     \/

if __name__ == '__main__':
    unittest.main()

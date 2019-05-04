#!/usr/bin/env python3
import sys
import os

(filePath, fileName) = os.path.split(__file__)
sys.path.insert(0,os.path.join(filePath, ".."))

import unittest
from texInterface import TexInterface
from humanTestFeedback import HumanTestFeedback

class TestTexInterface(unittest.TestCase):
    def setUp(self):
        self.texInterface = TexInterface()
        
    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        cls._humanTestFeedback = HumanTestFeedback()
        
    @classmethod
    def tearDownClass(cls):
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
        temp = self.texInterface.getTempF()
        message = ['For temp of board, is', '%.2f°F about right?' %temp]
        response = TestTexInterface._humanTestFeedback.msgToScreenGetResponse(message)
        self.assertTrue(response,
                    'Asking user if temperature is about %.2f°F' %temp)

        
if __name__ == '__main__':
    unittest.main()

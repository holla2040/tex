#!/usr/bin/env python3
import sys
import os

(filePath, fileName) = os.path.split(__file__)
sys.path.insert(0,os.path.join(filePath, ".."))

import unittest, time
from texInterface import TexInterface
from humanTestFeedback import HumanTestFeedback

class TestTexInterface(unittest.TestCase):
    def setUp(self):
        #print ("In setUp()")
        self.texInterface = TexInterface()
        self.humanTestFeedback = None
        
    def tearDown(self):
        #print ("In tearDown()")
        if self.humanTestFeedback:
            self.humanTestFeedback.cleanup(cleanUpGPIO=False)
        self.texInterface.cleanup()

    def createHumanTestFeedback(self):
        if not self.humanTestFeedback:
            self.humanTestFeedback = HumanTestFeedback()
        return self.humanTestFeedback

    @classmethod
    def setUpClass(cls):
        pass
        
    @classmethod
    def tearDownClass(cls):
        pass
    
    # Temperture Sensor Tests
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

    # Red, Green, Blue LED Tests
    def testBlueLed(self):
        imOK = False
        for i in range(2):
          self.texInterface.blueLightOn()
          time.sleep(.1)
          self.texInterface.blueLightOff()
          time.sleep(.1)
        imOK = True
        self.assertTrue(imOK,
                        'Flashing blue LED on and off twice')


    # LED Controller
    def testLedOnOff(self):
        imOK = False
        for i in range(2):
          self.texInterface.ledOn(0)
          time.sleep(.1)
          self.texInterface.ledOff(0)
          time.sleep(.1)
        imOK = True
        self.assertTrue(imOK,
                        'Flashing blue LED on and off twice')
    def testAllLedsOnOff(self):
        imOK = False
        for i in range(2):
          self.texInterface.ledAllOn()
          time.sleep(.1)
          self.texInterface.ledAllOff()
          time.sleep(.1)
        imOK = True
        self.assertTrue(imOK,
                        'Flashing blue LED on and off twice')
        

class TestTexInterfaceHuman(TestTexInterface):
    '''
    Class derived from base class TestTexInterface that will use
    base class's setUp() and tearDown() methods, and run all its
    tests.  But provides a way to not run the tests that require
    human interfention.  
    '''

    # Temperture Sensor Tests
    def testTempFViaHuman(self):
        humanTestFeedback = self.createHumanTestFeedback()
        temp = self.texInterface.getTempF()
        message = ['For temp of board, is', '%.2f°F about right?' %temp]
        response = humanTestFeedback.msgToScreenGetResponse(message)
        self.assertNotEqual(response,None,
                            'User responded by pushing yes or no button')
        self.assertTrue(response,
                    'Asking user if temperature is about %.2f°F' %temp)
        
        
if __name__ == '__main__':
    unittest.main()

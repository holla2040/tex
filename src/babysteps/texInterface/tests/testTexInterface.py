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
    def testLed1Blue(self):
        imOK = False
        for i in range(2):
          self.texInterface.blueLightOn()
          time.sleep(.1)
          self.texInterface.blueLightOff()
          time.sleep(.1)
        imOK = True
        self.assertTrue(imOK,
                        'Flashing blue LED on and off twice')
        
    def testLed2Red(self):
        imOK = False
        for i in range(2):
          self.texInterface.redLightOn()
          time.sleep(.1)
          self.texInterface.redLightOff()
          time.sleep(.1)
        imOK = True
        self.assertTrue(imOK,
                        'Flashing red LED on and off twice')

    def testLed3Green(self):
        imOK = False
        for i in range(2):
            self.texInterface.greenLightOn()
            time.sleep(.1)
            self.texInterface.greenLightOff()
            time.sleep(.1)
        imOK = True
        self.assertTrue(imOK,
                        'Flashing green LED on and off twice')

    def testLed4RedGreenBlue(self):
        imOK = False
        for i in range(2):
            self.texInterface.blueLightOn()
            time.sleep(.1)
            self.texInterface.redLightOn()
            time.sleep(.1)
            self.texInterface.greenLightOn()
            time.sleep(.1)
            
            self.texInterface.blueLightOff()
            time.sleep(.1)
            self.texInterface.redLightOff()
            time.sleep(.1)
            self.texInterface.greenLightOff()
            time.sleep(.1)
        imOK = True
        self.assertTrue(imOK,
                        'Flashing red LED on and off twice')


    # LED Controller
    def testLedOnOff(self):
        imOK = False
        for i in range(2):
            for channel in range(0,16):
                self.texInterface.ledOn(channel)
            time.sleep(.1)
            for channel in range(0,16):
                self.texInterface.ledOff(channel)
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
        
    def testFlashAllLeds(self):
        highLevelUp   = 1
        highLevelDown = .5
        lowLevel = .2
        sleepTime = .02
        self.texInterface.ledSetLevelAll(lowLevel)
        for channel in range(0, 16):
            with self.subTest(channel=channel):
                imOK = False
                self.texInterface.ledSetLevel(highLevelUp,channel)
                time.sleep(sleepTime)
                if channel > 0:
                    self.texInterface.ledSetLevel(lowLevel,channel-1)
                imOK = True
                self.assertTrue(imOK,
                                'Comparing level %s to %s on LED '% (highLevelUp,lowLevel)+\
                                '%s counting up' % (channel))
        for channel in range(15,-1,-1):
            with self.subTest(channel=channel):
                imOK = False
                self.texInterface.ledSetLevel(highLevelDown,channel)
                time.sleep(sleepTime)
                if channel < 15:
                    self.texInterface.ledSetLevel(lowLevel,channel+1)
                imOK = True
                self.assertTrue(imOK,
                                'Comparing level %s to %s on LED '% (highLevelDown,lowLevel)+\
                                '%s counting down' % (channel))
        self.texInterface.ledSetLevelAll(0)

    def testCurrentPowerMonitorVoltageCurrentPower(self):
        imOK = False
        supplyVoltage = self.texInterface.getSupplyVoltage_V()
        voltageBus = self.texInterface.getVoltageBus_V()
        voltageShunt = self.texInterface.getVoltageShunt_mV()
        current = self.texInterface.getCurrent_mA()
        power = self.texInterface.getPower_mW()
        msg =  'Got voltages, current and power from current/power monitor: '
        msg += 'sup=%.2fV, bus=%.2fV, ' % (supplyVoltage, voltageBus)
        msg += 'shunt=%.2fmV, I=%.2fmA, P=%.2fmW' % (voltageShunt, current, power)
        #print(msg)
        imOK = True
        self.assertTrue(imOK,msg)

    def testCurrentPowerMonitorSleepWakeOverflowReset(self):
        imOK = False
        self.texInterface.currentPowerMonitorSleep()
        time.sleep(0.5)
        self.texInterface.currentPowerMonitorWake()
        self.texInterface.getCurrentPowerMonitorCurrentOverflow()
        self.texInterface.currentPowerMonitorReset()
        imOK = True
        self.assertTrue(
            imOK, "Testing current/power monitor sleep, wake, current overflow and reset")
        
        
                        

class TestTexInterfaceHuman(TestTexInterface):
    '''
    Class derived from base class TestTexInterface that will use
    base class's setUp() and tearDown() methods, and run all its
    tests.  But provides a way to not run the tests that require
    human interfention.  
    '''

    # Temperture Sensor Tests
    def testViaHumanTempF(self):
        humanTestFeedback = self.createHumanTestFeedback()
        temp = self.texInterface.getTempF()
        message = ['For temp of board, is', '%.2f°F about right?' %temp]
        response = humanTestFeedback.msgToScreenGetResponse(message)
        self.assertNotEqual(response,None,
                            'User responded by pushing yes or no button')
        self.assertTrue(response,
                    'Asking user if temperature is about %.2f°F' %temp)
    
    def testViaHumanBlueLedOn(self):
        humanTestFeedback = self.createHumanTestFeedback()
        self.texInterface.blueLightOn()
        message = ['Is the blue LED on?']
        response = humanTestFeedback.msgToScreenGetResponse(message)
        self.texInterface.blueLightOff()
        self.assertNotEqual(response,None,
                            'User responded by pushing yes or no button')
        self.assertTrue(response,
                        'Asking user if the blue LED is on')
    
    def testViaHumanRedLedOn(self):
        humanTestFeedback = self.createHumanTestFeedback()
        self.texInterface.redLightOn()
        message = ['Is the red LED on?']
        response = humanTestFeedback.msgToScreenGetResponse(message)
        self.assertNotEqual(response,None,
                            'User responded by pushing yes or no button')
        self.assertTrue(response,
                        'Asking user if the red LED is on')

    def testViaHumanGreenLedOn(self):
        humanTestFeedback = self.createHumanTestFeedback()
        self.texInterface.greenLightOn()
        message = ['Is the green LED on?']
        response = humanTestFeedback.msgToScreenGetResponse(message)
        self.assertNotEqual(response,None,
                            'User responded by pushing yes or no button')
        self.assertTrue(response,
                        'Asking user if the green LED is on')

        
if __name__ == '__main__':
    unittest.main()

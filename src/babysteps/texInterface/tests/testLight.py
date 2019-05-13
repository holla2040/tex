#!/usr/bin/env python3
import sys
import os

(filePath, fileName) = os.path.split(__file__)
sys.path.insert(0,os.path.join(filePath, ".."))

import unittest, time
from lights import Light
from texInterface import TexInterface

class TestLightBase(unittest.TestCase):
    def setUp(self):
        #print ("In setUp()")
        self.texInterface = TexInterface()
        
    def tearDown(self):
        #print ("In tearDown()")
        self.texInterface.cleanup()

    @classmethod
    def setUpClass(cls):
        pass
        
    @classmethod
    def tearDownClass(cls):
        pass

class TestLight(TestLightBase):
    def testLightInit(self):
        light = Light()
        self.assertEqual(light.texInterface, None,"Checking light.texInterface")
        self.assertEqual(light.ledNumber   , None,"Checking light.ledNumber   ")
        self.assertEqual(light.onLightLevel, None,"Checking light.onLightLevel")
        self.assertEqual(light.lightLevel  , None,"Checking light.lightLevel  ")
        self.assertEqual(light.lightMode   , None,"Checking light.lightMode   ")

    def testLightSetup(self):
        light = Light()
        light.setup(self.texInterface, 0, Light.LEVEL.HIGH*.8)
        self.assertEqual(light.texInterface, self.texInterface,
                         "Checking light.texInterface")
        self.assertEqual(light.ledNumber   , 0,
                         "Checking light.ledNumber   ")
        self.assertEqual(light.onLightLevel, Light.LEVEL.HIGH*.8,
                         "Checking light.onLightLevel")
        self.assertEqual(light.lightLevel  , Light.LEVEL.LOW,
                         "Checking light.lightLevel  ")
        self.assertEqual(light.lightMode   , Light.MODE.LIGHT_OFF,
                         "Checking light.lightMode   ")
        light.cleanup()

    def testLightOff(self):
        light = Light()
        light.setup(self.texInterface, 0, Light.LEVEL.HIGH*.8)
        light.off()
        self.assertEqual(light.lightLevel  , Light.LEVEL.LOW,
                         "Checking light.lightLevel  ")
        self.assertEqual(light.lightMode   , Light.MODE.LIGHT_OFF,
                         "Checking light.lightMode   ")
        light.cleanup()

    def testLightOn(self):
        light = Light()
        light.setup(self.texInterface, 0, Light.LEVEL.HIGH*.8)
        light.on()
        self.assertEqual(light.lightLevel  , Light.LEVEL.HIGH*.8,
                         "Checking light.lightLevel  ")
        self.assertEqual(light.lightMode   , Light.MODE.LIGHT_ON,
                         "Checking light.lightMode   ")
        light.cleanup()

    def testLightToggle(self):
        light = Light()
        light.setup(self.texInterface, 0, Light.LEVEL.HIGH*.8)
        light.on()
        self.assertEqual(light.lightLevel  , Light.LEVEL.HIGH*.8,
                         "Checking light.lightLevel  ")
        self.assertEqual(light.lightMode   , Light.MODE.LIGHT_ON,
                         "Checking light.lightMode   ")
        light.toggle() # Turn off
        self.assertEqual(light.lightLevel  , Light.LEVEL.LOW,
                         "Checking light.lightLevel  ")
        self.assertEqual(light.lightMode   , Light.MODE.LIGHT_OFF,
                         "Checking light.lightMode   ")
        light.toggle() # Turn on
        self.assertEqual(light.lightLevel  , Light.LEVEL.HIGH*.8,
                         "Checking light.lightLevel  ")
        self.assertEqual(light.lightMode   , Light.MODE.LIGHT_ON,
                         "Checking light.lightMode   ")
        light.toggle() # Turn off
        self.assertEqual(light.lightLevel  , Light.LEVEL.LOW,
                         "Checking light.lightLevel  ")
        self.assertEqual(light.lightMode   , Light.MODE.LIGHT_OFF,
                         "Checking light.lightMode   ")
        light.cleanup()

    def testLightSetOnLightLevel(self):
        light = Light()
        light.setup(self.texInterface, 0, Light.LEVEL.HIGH*.8)
        light.setOnLightLevel(Light.LEVEL.HIGH*.2)
        self.assertEqual(light.lightLevel  , Light.LEVEL.LOW,
                         "Checking light.lightLevel  ")
        self.assertEqual(light.onLightLevel, Light.LEVEL.HIGH*.2,
                         "Checking light.onLightLevel  ")
        self.assertEqual(light.lightMode   , Light.MODE.LIGHT_OFF,
                         "Checking light.lightMode   ")
        light.on()
        self.assertEqual(light.lightLevel  , Light.LEVEL.HIGH*.2,
                         "Checking light.lightLevel  ")
        self.assertEqual(light.onLightLevel, Light.LEVEL.HIGH*.2,
                         "Checking light.onLightLevel  ")
        self.assertEqual(light.lightMode   , Light.MODE.LIGHT_ON,
                         "Checking light.lightMode   ")
        light.setOnLightLevel(Light.LEVEL.HIGH*.4)
        self.assertEqual(light.lightLevel  , Light.LEVEL.HIGH*.4,
                         "Checking light.lightLevel  ")
        self.assertEqual(light.onLightLevel , Light.LEVEL.HIGH*.4,
                         "Checking light.onLightLevel  ")
        self.assertEqual(light.lightMode   , Light.MODE.LIGHT_ON,
                         "Checking light.lightMode   ")
        light.off()
        light.setOnLightLevel(Light.LEVEL.HIGH*.6)
        self.assertEqual(light.lightLevel  , Light.LEVEL.LOW,
                         "Checking light.lightLevel  ")
        self.assertEqual(light.onLightLevel , Light.LEVEL.HIGH*.6,
                         "Checking light.onLightLevel  ")
        self.assertEqual(light.lightMode   , Light.MODE.LIGHT_OFF,
                         "Checking light.lightMode   ")
        light.cleanup()

    def testIncrementOnLightLevel(self):
        light = Light()
        light.setup(self.texInterface, 0, Light.LEVEL.HIGH*.8)
        light.incrementOnLightLevel(-Light.LEVEL.HIGH*.2)
        self.assertLess(abs(light.lightLevel-Light.LEVEL.LOW),1e-6,
                               "Checking light.lightLevel  ")
        self.assertLess(abs(light.onLightLevel-Light.LEVEL.HIGH*.6),1e-6,
                        "Checking light.onLightLevel")
        self.assertEqual(light.lightMode   , Light.MODE.LIGHT_OFF,
                         "Checking light.lightMode   ")
        light.on()
        self.assertLess(abs(light.lightLevel-Light.LEVEL.HIGH*.6),1e-6,
                        "Checking light.lightLevel  ")
        self.assertLess(abs(light.onLightLevel-Light.LEVEL.HIGH*.6),1e-6,
                               "Checking light.onLightLevel  ")
        self.assertEqual(light.lightMode   , Light.MODE.LIGHT_ON,
                         "Checking light.lightMode   ")
        light.incrementOnLightLevel(-Light.LEVEL.HIGH*.2)
        self.assertLess(abs(light.lightLevel-Light.LEVEL.HIGH*.4),1e-6,
                               "Checking light.lightLevel  ")
        self.assertLess(abs(light.onLightLevel-Light.LEVEL.HIGH*.4),1e-6,
                               "Checking light.onLightLevel  ")
        self.assertEqual(light.lightMode   , Light.MODE.LIGHT_ON,
                         "Checking light.lightMode   ")
        light.incrementOnLightLevel(-Light.LEVEL.HIGH)
        self.assertLess(abs(light.lightLevel-0),1e-6,
                               "Checking light.lightLevel  ")
        self.assertLess(abs(light.onLightLevel-0),1e-6,
                               "Checking light.onLightLevel  ")
        self.assertEqual(light.lightMode   , Light.MODE.LIGHT_ON,
                         "Checking light.lightMode   ")
        light.incrementOnLightLevel(Light.LEVEL.HIGH*2)
        self.assertLess(abs(light.lightLevel-Light.LEVEL.HIGH),1e-6,
                               "Checking light.lightLevel  ")
        self.assertLess(abs(light.onLightLevel-Light.LEVEL.HIGH),1e-6,
                               "Checking light.onLightLevel  ")
        self.assertEqual(light.lightMode   , Light.MODE.LIGHT_ON,
                         "Checking light.lightMode   ")
        light.off()
        light.cleanup()

    def testGetLightMode(self):
        light = Light()
        self.assertEqual(light.getLightMode(), None)
        light.setup(self.texInterface, 0, Light.LEVEL.HIGH*.8)
        self.assertEqual(light.getLightMode(), Light.MODE.LIGHT_OFF)
        light.on()
        self.assertEqual(light.getLightMode(), Light.MODE.LIGHT_ON)
        light.off()
        self.assertEqual(light.getLightMode(), Light.MODE.LIGHT_OFF)
        light.cleanup()

        

    def testLightflash(self):
        highLevelUp   = 1
        highLevelDown = .5
        lowLevel = .2
        sleepTime = .02
        lightArray = [Light(), Light(), Light(), Light(),
                      Light(), Light(), Light(), Light(),
                      Light(), Light(), Light(), Light(),
                      Light(), Light(), Light(), Light() ]
        for channel in range (0,16):
            lightArray[channel].setup(self.texInterface, channel, lowLevel)
            lightArray[channel].on()

        for channel in range(0, 16):
            with self.subTest(channel=channel):
                imOK = False
                lightArray[channel].setOnLightLevel(highLevelUp)
                time.sleep(sleepTime)
                if channel > 0:
                    lightArray[channel-1].setOnLightLevel(lowLevel)
                imOK = True
                self.assertTrue(imOK,
                                'Comparing level %s to %s on LED '% (highLevelUp,lowLevel)+\
                                '%s counting up' % (channel))
        for channel in range(15,-1,-1):
            with self.subTest(channel=channel):
                imOK = False
                lightArray[channel].setOnLightLevel(highLevelDown)
                time.sleep(sleepTime)
                if channel < 15:
                    lightArray[channel+1].setOnLightLevel(lowLevel)
                imOK = True
                self.assertTrue(imOK,
                                'Comparing level %s to %s on LED '% (highLevelDown,lowLevel)+\
                                '%s counting down' % (channel))
        for light in lightArray:
            light.off()
            light.cleanup()
        
if __name__ == '__main__':
    unittest.main()

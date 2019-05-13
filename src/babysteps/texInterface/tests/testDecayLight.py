#!/usr/bin/env python3
import sys
import os

(filePath, fileName) = os.path.split(__file__)
sys.path.insert(0,os.path.join(filePath, ".."))

import unittest, time
from lights import Light,DecayLight
from testLight import TestLightBase
from texInterface import TexInterface

class TestDecayLight(TestLightBase):
    def testInit(self):
        light = DecayLight()
        self.assertEqual(light.texInterface, None,"Checking light.texInterface")
        self.assertEqual(light.ledNumber   , None,"Checking light.ledNumber   ")
        self.assertEqual(light.onLightLevel, None,"Checking light.onLightLevel")
        self.assertEqual(light.lightLevel  , None,"Checking light.lightLevel  ")
        self.assertEqual(light.lightMode   , None,"Checking light.lightMode   ")
        self.assertEqual(light.decayStartTime,0,"Checking light.decayStartTime")
        self.assertEqual(light.changeTime,0,"Checking light.changeTime")
        self.assertEqual(light.decaying          ,False,"Checking light.decaying")
        self.assertEqual(light.intervalIndex     ,0    ,
                         "Checking light.intervalIndex")     
        self.assertEqual(light.numIntervals      ,None ,
                         "Checking light.numIntervals")
        self.assertEqual(light.onLengthArray     ,None ,
                         "Checking light.onLengthArray") 
        self.assertEqual(light.decayLengthArray  ,None ,
                         "Checking light.decayLengthArray")
        self.assertEqual(light.maxLightLevelArray,None ,
                         "Checking light.maxLightLevelArray")
        self.assertEqual(light.tauArray          ,None ,
                         "Checking light.tauArray")

    def testSetup(self):
        maxLightLevel      = Light.LEVEL.HIGH*.8,
        onLengthArray      = [1,1,1]
        decayLengthArray   = [1,1,1]
        maxLightLevelArray = [maxLightLevel,maxLightLevel,maxLightLevel]
        tauArray           = [.001, .001, .001]
        light = DecayLight()
        light.setup(self.texInterface, 0, Light.LEVEL.HIGH*.8,
                    onLengthArray, decayLengthArray, maxLightLevelArray,
                    tauArray)
        # Vars set in Light base class and not overwritten in DecayLight
        self.assertEqual(light.texInterface, self.texInterface,
                         "Checking light.texInterface")
        self.assertEqual(light.ledNumber     , 0,
                         "Checking light.ledNumber   ")
        self.assertEqual(light.onLightLevel  , Light.LEVEL.HIGH*.8,
                         "Checking light.onLightLevel")
        # Set in DecayLight class
        self.assertEqual(light.numIntervals  ,len(tauArray),
                         "Checking  light.numIntervals")
        self.assertEqual(light.lightLevel    ,light.LEVEL.LOW,
                         "Checking  light.lightMode")
        self.assertEqual(light.lightMode     ,light.MODE.LIGHT_FLASHING,
                         "Checking light.lightMode")
        self.assertEqual(light.onLengthArray ,onLengthArray,
                         "Checking light.onLength")
        self.assertEqual(light.decayLengthArray,decayLengthArray,
                         "Checking light.decayLength")
        self.assertEqual(light.maxLightLevelArray , maxLightLevelArray,
                         "Checking light.maxLightLevel")
        self.assertEqual(light.tauArray      ,tauArray,
                         "Checking light.tauArray")
        self.assertEqual(light.changeTime    ,0,
                         "Checking light.changeTime")
        self.assertEqual(light.decaying      ,True,
                         "Checking light.decaying")
        self.assertEqual(light.decayStartTime,0 ,
                         "Checking light.decayStartTime")
        self.assertEqual(light.intervalIndex ,0 ,
                         "Checking light.intervalIndex")
        
    def testGetLightMode(self):
        # Needs code
        pass

    @unittest.skip("Not really a unittest")
    def testUpdateWithF16Data(self):
        maxLightLevel      = Light.LEVEL.HIGH

        positionOnLengthArray      = [.1]  # On : .1s
        positionDecayLengthArray   = [1.1] # Off: 1.2s
        positionMaxLightLevelArray = [Light.LEVEL.HIGH] # Full power
        positionTauArray           = [.1]  # .1s time const

        collisionOnLengthArray      = [.05,  .05]  # On : .05s, .05s
        collisionDecayLengthArray   = [.25, 1.500] # Off: .25s, then 1.5 s
        collisionMaxLightLevelArray = [Light.LEVEL.HIGH*.1,
                                       Light.LEVEL.HIGH*.1] # Full on
        collisionTauArray           = [None,None] # On/Off, no decay

        positionLight = DecayLight()
        collisionLight = DecayLight()

        positionLight.setup(self.texInterface, 0, Light.LEVEL.HIGH*.8,
                            positionOnLengthArray, positionDecayLengthArray,
                            positionMaxLightLevelArray, positionTauArray)
        collisionLight.setup(self.texInterface, 1, Light.LEVEL.HIGH*.8,
                            collisionOnLengthArray, collisionDecayLengthArray,
                            collisionMaxLightLevelArray, collisionTauArray)
        positionLight.flash()
        collisionLight.flash()
        try:
            while True:
                positionLight.update()
                collisionLight.update()
                time.sleep(.008)
        except KeyboardInterrupt:
            print('\nCaught KeyboardInterrupt, exiting test...')
        positionLight.off()
        
        
if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python3
import sys
import os

(filePath, fileName) = os.path.split(__file__)
sys.path.insert(0,os.path.join(filePath, ".."))

import time
from lights import Light,DecayLight
from texInterface import TexInterface

class ShoeBoxF16():
    def setup(self):
        self.texInterface = TexInterface()

        maxLightLevel      = Light.LEVEL.HIGH

        positionOnLengthArray      = [.1]  # On : .1s
        positionDecayLengthArray   = [1.1] # Off: 1.1s
        positionMaxLightLevelArray = [Light.LEVEL.HIGH] # Full power
        positionTauArray           = [.1]  # .1s time const

        collisionOnLengthArray      = [.05,  .05]  # On : .05s, .05s
        collisionDecayLengthArray   = [.25, 1.500] # Off: .25s, then 1.5 s
        collisionMaxLightLevelArray = [Light.LEVEL.HIGH*.1,
                                       Light.LEVEL.HIGH*.1] # Full on
        collisionTauArray           = [None,None] # On/Off, no decay

        self.positionLight = DecayLight()
        self.collisionLight = DecayLight()

        self.positionLight.setup(self.texInterface, 0, Light.LEVEL.HIGH*.8,
                            positionOnLengthArray, positionDecayLengthArray,
                            positionMaxLightLevelArray, positionTauArray)
        self.collisionLight.setup(self.texInterface, 1, Light.LEVEL.HIGH*.8,
                            collisionOnLengthArray, collisionDecayLengthArray,
                            collisionMaxLightLevelArray, collisionTauArray)
        self.positionLight.flash()
        self.collisionLight.flash()

    def run(self):
        downTime = .013 #seconds
        timeLocal = time.time
        while True:
            startTime = timeLocal()
            self.positionLight.update()
            self.collisionLight.update()
            elapsedTime = timeLocal()-startTime
            sleepTime = downTime - elapsedTime
            #print ("startTime = {}, elapsedTime = {}, sleepTime = {}".format(startTime,elapsedTime,sleepTime))
            if (sleepTime > 0):
                time.sleep(sleepTime)

    def cleanup(self):
        self.positionLight.cleanup()
        self.collisionLight.cleanup()
        self.texInterface.cleanup()
        
if __name__ == '__main__':
    shoeBoxF16 = ShoeBoxF16()
    shoeBoxF16.setup()
    try:
        shoeBoxF16.run()
    except KeyboardInterrupt:
        print("\nCaught KeyboardInterrupt. ",end="")

    print("Cleaning up and exiting...")
    shoeBoxF16.cleanup()


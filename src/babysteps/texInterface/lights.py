#!/usr/bin/env python3

import sys, os
(filePath, fileName) = os.path.split(__file__)
sys.path.insert(0,os.path.join(filePath, "lib"))

class Light():

    class MODE():
        LIGHT_MODE_NOTSET = -1
        LIGHT_OFF = 0
        LIGHT_ON  = 1
        LIGHT_FLASHING = 2

    class LEVEL():
        ON  = 1
        OFF = 0
        
    def __init__(self,debug=False):
        self.debug = debug

        self.texInterface = None
        self.ledNumber    = None
        self.onLightLevel = None
        self.lightLevel   = None
        self.lightMode    = None

    def setup(self, texInterface, ledNumber, onLightLevel):
        self.texInterface = texInterface
        self.ledNumber    = ledNumber
        self.onLightLevel = onLightLevel
        self.off();

    def update(self):
        self.texInterface.ledSetLevel(self.lightLevel, self.ledNumber)

    def off(self):
        self.lightLevel = Light.LEVEL.OFF;
        self.lightMode  = Light.MODE.LIGHT_OFF
        self.update()

    def on(self):
        self.lightLevel = self.onLightLevel
        self.lightMode  = Light.MODE.LIGHT_ON
        self.update()

    def toggle(self):
        if (self.lightMode == Light.MODE.LIGHT_MODE_NOTSET or
            self.lightMode == Light.MODE.LIGHT_FLASHING):
            pass
        elif self.lightMode == Light.MODE.LIGHT_OFF:
            self.on();
        elif self.lightMode == Light.MODE.LIGHT_ON:
            self.off();

    def setOnLightLevel(self, onLightLevel):
        self.onLightLevel = onLightLevel;
        if (self.lightMode == Light.MODE.LIGHT_ON):
            self.on();

    def incrementOnLightLevel(self, onLightLevelIncrement):
        onLightLevelValue = self.onLightLevel + onLightLevelIncrement;
        if (onLightLevelValue > Light.MODE.LIGHT_ON):
            onLightLevelValue = Light.MODE.LIGHT_ON
        elif (onLightLevelValue < Light.MODE.LIGHT_OFF):
            onLightLevelValue = Light.MODE.LIGHT_OFF;
        self.setOnLightLevel(onLightLevelValue);
  
    def getLightMode(self):
        return self.lightMode


if __name__ == "__main__":
    light = Light()
    light.setup()
    light.dump()
    
    

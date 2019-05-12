#!/usr/bin/env python3

import sys, os, math
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
        print ("In Light.__init__(debug)")
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

class DecayLight(Light):
    """
    A light that is on, then switches off, but filament "cools" when light
    is switched off.
    For each interval, specify length of time 'onLength' light is on at
    'maxLightLevel'.  Then, for each interval, specify 'decayLength' how long
    light will spend in decay mode, which is either moving to off or off.
    Length of time moving to off (i.e. decaying) is governed by 'tau' and
    Newton's law of cooling, as desribed below.
  
    In this class the light level decays at a rate given by Newton's
    law of cooling, which is
   
    T = T_env + dT*exp(-t/tau)
    where:
      t = time
      tau = time constant
      T = Temperature at time t
      T_env = Temperature of the surrounding environment
      dT = Initial temperature difference in bodies (T_0 - T_env)
      T_0 = Temperature at time 0.
   
      tau = ro*V*c_p/h*A_s
      ro = density
      V = volume
      c_p = heat capacity
      A_s = surface area
      h = heat transfer coefficient
  
    Note:
    At t=0, T = T_0 = T_env + dT
    At t=tau,   T will have decreased by 63.2% to .368*dT
    At t=2*tau, T will have decreased by 86.5% to .135*dT  
   
    For us T_env = 0 and dT = maxLightLevel so
    light_level = maxLightLevel*exp(-time/(tau))
    where tau is given in seconds
    """

    def __init__(self,debug=False):
        print ("In DecayLight.__init__(debug)")
        super().__init__(debug)
        self.decayStartTime  = 0 # Keep track of when decay started.
        self.changeTime      = 0 # Keep track of when its time to change modes
        self.decaying        = False # Bool if in on or decay mode
        self.intervalIndex   = 0 # Keep track which lighting inverval we are on
        self.numIntervals    = None # Length of arrays

        self.onLengthArray   = None # Time to stay on before switching to 
                                    # decay mode, for each interval
        self.decayLengthArray= None # Time to stay in decay mode, before 
                                    # starting next interval, for each interval
        self.maxLightLevelArray = None # Light level when on, for each interval
        self.tauArray        = None # Time constants in secs. See discussion above

        def setup(texInterface, ledNumber, onLightLevel,
                  onLengthArray, decayLengthArray,
                  maxLightLevelArray, tauArray):
            super().setup(texInterface, ledNumber, onLightLevl)
            assert(len(onLengthArray) == len(decayLengthArray) ==
                   len(maxLightLevelArray) == len(tauArray),
                   "Expecting all array lenghts to be the same. "+\
                   "len(onLengthArray) = %s, " % len(onLengthArray) +\
                   "len(decayLengthArray) = %s, " % len(decayLengthArray) +\
                   "len(maxLightLevelArray) = %s, " % len(maxLightLevelArray) +\
                   "len(tauArray) = %s, " % len(tauArray))
            self.numIntervals = len(onLengthArray)
            # Overide call to off() made in Light::setup since we want this light
            # to be in flashing mode right away
            self.lightLevel = Light.LIGHT_LEVEL.OFF # Set the initial light level
            self.lightMode = Light.MODE.LIGHT_FLASHING

            self.onLength = onLengthValues;
            self.decayLength = decayLengthValues;
            self.maxLightLevel = maxLightLevelValues;
            self.tauArray = tauArray

            self.changeTime     = 0    # Change right away
            self.decaying       = True # Will cause us to go to on mode right away
            self.decayStartTime = 0
            self.intervalIndex  = 0    # Will be incremented during first
                                       # call to update
            
  
        def flash(self):
            self.lightLevel = maxLightLevelArray(self.intervalIndex)
            self.lightMode = LIGHT_FLASHING
            self.on()
            
        def getDecaying(sefl):
            return self.decaying

        def update(self):
            #print ("In update() A"));
            j = 0

            changeTimeDelta = 0;
  
            now = time.time()
            j = self.intervalIndex % self.numIntervals;
  
            if (now >= self.changeTime):
                if (self.decaying):
                    # print ("In update() B")
                    self.decaying = false
                    self.intervalIndex += 1
                    j = self.intervalIndex % self.numIntervals;
                    if (self.lightMode == Light.MODE.LIGHT_FLASHING):
                        self.lightLevel = self.maxLightLevelArray[j]
                    self.changeTimeDelta = self.onLengthArray[j]
                else:
                    # println("In update() C")
                    self.decaying = True
                    self.changeTimeDelta = self.decayLengthArray[j]
                self.decayStartTime = self.changeTime;
                self.changeTime = self.changeTime + self.changeTimeDelta;
                # Check if time between calls to update() is > onLengthArray[j]
                # or decayLengthArray[j]
                if (now >= self.changeTime):
                    # print("In update() D")
                    self.decayStartTime = now
                    self.changeTime = now + changeTimeDelta
                    # print ("decayStartTime, changeTime, decaying = ",
                    #        self.decayStartTime,", ",self.changeTime,", ",
                    #        self.decaying,sep="",file=sys.stderr)

            # print("In update() E")
            if (self.decaying and self.lightMode == Light.MODE.LIGHT_FLASHING):
                # print("A",file=sys.stderr)
                if (self.tauArray[j] == 0):
                    # print("B",file=sys.stderr)
                    self.lightLevel = Light.LIGHT_LEVEL.OFF;
                else:
                    # print("In update() F")
                    # print("C",file=sys.stderr)
                    decayTime = now - self.decayStartTime # How long we have been decaying
                    # print("now", now ,file=sys.stderr)
                    # print("decayTime", decayTime,file=sys.stderr)
                    # T = dT*e(-t/tau)  // T = Dt @ t=0, T = 0 @ t = infinity
                    self.lightLevel = self.maxLightLevelArray[j]*\
                                      math.exp(-(decayTime)/(tauArray[j]));
                    # print("lightLevel", lightLevel, file=sys.stderr)

                # print("F",file=sys.stderr)

                # print ("now =",now,
                #        "self.decayStartTime =", self.decayStartTime,
                #        "self.changeTime  =", self.changeTime,
                #        "self.numIntervals =", self.numIntervals,
                #        "self.intervalIndex =", sefl.intervalIndex,
                #        "j =", j, "\n",
                #        "self.decaying =",self.decaying,
                #        "self.lightLevel =" << self.lightLevel,
                #        "self.tauArray  =" << self.tauArray[j],file=sys.stderr)

if __name__ == "__main__":
    print ("Instantiating a Light object")
    light = Light()
    print ("Instantiating a DecayLight object")
    decayLight = DecayLight()

#!/usr/bin/env python3

from temperatureSensor import TemperatureSensor
import RPi.GPIO as gpio
import Adafruit_PCA9685
import sys

class TexInterface():

    # LED controller is a PWM, pulse width modulation, controller
    fPWM = 50 # Frequencey of led controller. Range 40-1000Hz
    ledLow = 0
    ledHigh = 4095 # PWM has 12 bits of resolution: 0 to 2^12-1 = 0 to 4095
    ledControllerAddress = 0x60
    tempSensorAddress = 0x4C
    ledPinRed = 9
    ledPinGreen = 11
    ledPinBlue = 8
    
    def __init__(self,debug=False):
        self.debug = debug

        self.tempSensor = None
        self.ledController = None

        gpio.setmode(gpio.BCM)
        gpio.setup(TexInterface.ledPinRed, gpio.OUT)
        gpio.setup(TexInterface.ledPinGreen, gpio.OUT)
        gpio.setup(TexInterface.ledPinBlue, gpio.OUT)

    def cleanup(self,cleanUpGPIO=True):
        if cleanUpGPIO:
            gpio.cleanup()
        
    def helloWorld(self):
        print("Hello world")


    # Temperature Sensor
    def createTempSensor(self):
        if None == self.tempSensor:
            self.tempSensor = TemperatureSensor(address=TexInterface.tempSensorAddress)

    def getTempC(self):
        self.createTempSensor()
        return self.tempSensor.getTempC()
    
    def getTempF(self):
        self.createTempSensor()
        return self.tempSensor.getTempF()

    # Red, Grean and Blue LED
    def blueLightOn(self):
        gpio.output(TexInterface.ledPinBlue, gpio.HIGH)

    def blueLightOff(self):
        gpio.output(TexInterface.ledPinBlue, gpio.LOW)

    # LED Controller
    def createLedController(self):
        if None == self.ledController:
            self.ledController = Adafruit_PCA9685.PCA9685(address=TexInterface.ledControllerAddress)  # This takes additional arguments: address and i2c
            self.ledController.set_pwm_freq(TexInterface.fPWM) #Set the PWM frequency in hertz
    def ledSetLevel(self, level, ledNumber):
        '''
        Set light level to 'level' of led number 'ledNumber'
        where level is a float between 0 and 1 and ledNumber
        is an integer representing led 0 to 15
        '''
        if not (isinstance(level, float) or isinstance(level, int)):
            msg = "Argument level is of the wrong type sent to "+\
                  "TexInterface.ledSetLevel(level=%s,ledNumber=%s). " % (level, ledNumber)+\
                  "Expection float or int but got %s" % type(level)
            raise TypeError(msg)
        if not isinstance(ledNumber, int):
            msg = "Argument ledNumber is of the wrong type sent to "+\
                  "TexInterface.ledSetLevel(level=%s,ledNumber=%s). " % (level, ledNumber)+\
                  "Expection float or int but got %s" % type(ledNumber)
            raise TypeError(msg)
        if (level < 0 or level > 1):
            msg = "Bad value of level sent to "+\
                  "TexInterface.ledSetLevel(level=%s,ledNumber=%s). " % (level, ledNumber)+\
                  "Expeced float between 0 and 1"
            raise ValueError(msg)
        if (ledNumber < 0 or ledNumber > 15):
            msg = "Bad value of ledNumber sent to "+\
                  "TexInterface.ledSetLevel(level=%s,ledNumber=%s). " % (level, ledNumber)+\
                  "Expeced integer between 0 and 15"
            raise ValueError(msg)
        self.createLedController()
        self.ledController.set_pwm(ledNumber,0,int(level*TexInterface.ledHigh))

    def ledOff(self,ledNumber):
        self.ledSetLevel(0,ledNumber)

    def ledOn(self,ledNumber):
        self.ledSetLevel(1,ledNumber)

    def ledAllOff(self):
        for ledNumber in range (16):
            self.ledOff(ledNumber)
            
    def ledAllOn(self):
        for ledNumber in range (16):
            self.ledOn(ledNumber)
    

    if __name__ == "__main__":
        tex = TexInterface()
        tex.helloWorld()
    

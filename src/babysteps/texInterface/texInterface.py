#!/usr/bin/env python3

import sys, os
(filePath, fileName) = os.path.split(__file__)
sys.path.insert(0,os.path.join(filePath, "lib"))

from temperatureSensor import TemperatureSensor
import RPi.GPIO as gpio # ToDo: Change this to Adafruit_GPIO
import Adafruit_PCA9685
from ina219 import INA219 # Only a Adafruit CircuitPython driver is available
from ina219 import DeviceRangeError

class TexInterface():

    class PWM_LIGHT_LEVEL:
        LOW = 0.0
        HIGH = 1.0

    # LED controller is a PWM, pulse width modulation, controller
    fPWM = 50 # Frequencey of led controller. Range 40-1000Hz
    ledLow = 0
    ledHigh = 4095 # PWM has 12 bits of resolution: 0 to 2^12-1 = 0 to 4095
    ledControllerAddress = 0x60
    tempSensorAddress = 0x4C
    ledPinRed = 11
    ledPinGreen = 9 
    ledPinBlue = 8
    shunt_ohms = 0.15   # for INA219 current sensor

    
    def __init__(self,debug=False):
        self.debug = debug

        self.tempSensor = None
        self.ledController = None
        self.currentPowerMonitor = None

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

    def redLightOn(self):
        gpio.output(TexInterface.ledPinRed, gpio.HIGH)

    def redLightOff(self):
        gpio.output(TexInterface.ledPinRed, gpio.LOW)

    def greenLightOn(self):
        gpio.output(TexInterface.ledPinGreen, gpio.HIGH)

    def greenLightOff(self):
        gpio.output(TexInterface.ledPinGreen, gpio.LOW)
    
    # LED Controller
    def createLedController(self):
        if None == self.ledController:
            self.ledController = Adafruit_PCA9685.PCA9685(address=TexInterface.ledControllerAddress)  # This takes additional arguments: address and i2c
            self.ledController.set_pwm_freq(TexInterface.fPWM) #Set the PWM frequency in hertz
            
    def ledSetLevel(self, level, ledNumber):
        '''
        Set light level to 'level' of led number 'ledNumber'
        where level is a float between TexInterface.PWM_LIGHT_LEVEL.LOW and TexInterface.PWM_LIGHT_LEVEL.HIGH
        and ledNumber is an integer representing led 0 to 15
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
        if (level < TexInterface.PWM_LIGHT_LEVEL.LOW or level > TexInterface.PWM_LIGHT_LEVEL.HIGH):
            msg = "Bad value of level sent to "+\
                  "TexInterface.ledSetLevel(level=%s,ledNumber=%s). " % (level, ledNumber)+\
                  "Expeced float between " +\
                  "TexInterface.PWM_LIGHT_LEVEL.LOW(=%s) " % TexInterface.PWM_LIGHT_LEVEL.LOW +\
                  "and TexInterface.PWM_LIGHT_LEVEL.HIGH(=%s)" % TexInterface.PWM_LIGHT_LEVEL.LOW
            raise ValueError(msg)
        if (ledNumber < 0 or ledNumber > 15):
            msg = "Bad value of ledNumber sent to "+\
                  "TexInterface.ledSetLevel(level=%s,ledNumber=%s). " % (level, ledNumber)+\
                  "Expeced integer between 0 and 15"
            raise ValueError(msg)
        self.createLedController()
        self.ledController.set_pwm(ledNumber,0,int(level*TexInterface.ledHigh))

    def ledOff(self,ledNumber):
        self.ledSetLevel(TexInterface.PWM_LIGHT_LEVEL.LOW,ledNumber)

    def ledOn(self,ledNumber):
        self.ledSetLevel(TexInterface.PWM_LIGHT_LEVEL.HIGH,ledNumber)

    def ledAllOff(self):
        for ledNumber in range (16):
            self.ledOff(ledNumber)
            
    def ledAllOn(self):
        for ledNumber in range (16):
            self.ledOn(ledNumber)
            
    def ledSetLevelAll(self,level):
        for ledNumber in range (16):
            self.ledSetLevel(level,ledNumber)
    
    # Current/Power Monitor
    def createCurrentPowerMonitor(self):
        if None == self.currentPowerMonitor:
            self.currentPowerMonitor = INA219(TexInterface.shunt_ohms)
            self.currentPowerMonitor.configure()

    def getSupplyVoltage_V(self):
        """ Returns the bus supply voltage in volts. This is the sum of
        the bus voltage and shunt voltage. A DeviceRangeError
        exception is thrown if current overflow occurs."""
        self.createCurrentPowerMonitor()
        return self.currentPowerMonitor.supply_voltage()

    def getVoltageBus_V(self):
        """ Returns the bus voltage in volts. """
        self.createCurrentPowerMonitor()
        return self.currentPowerMonitor.voltage()

    def getVoltageShunt_mV(self):
        """ Returns the shunt voltage in millivolts.
        A DeviceRangeError exception is thrown if current overflow occurs."""
        self.createCurrentPowerMonitor()
        return self.currentPowerMonitor.shunt_voltage()

    def getCurrent_mA(self):
        """ Returns the bus current in milliamps. A DeviceRangeError
        exception is thrown if current overflow occurs."""
        self.createCurrentPowerMonitor()
        return self.currentPowerMonitor.current()

    def getPower_mW(self):
        """ Returns the bus power consumption in milliwatts.
        A DeviceRangeError exception is thrown if current overflow occurs."""
        self.createCurrentPowerMonitor()
        return self.currentPowerMonitor.power()

    def currentPowerMonitorSleep(self):
        """ Put the INA219 into power down mode. """
        self.createCurrentPowerMonitor()
        return self.currentPowerMonitor.sleep()

    def currentPowerMonitorWake(self):
        """ Wake the INA219 from power down mode """
        self.createCurrentPowerMonitor()
        return self.currentPowerMonitor.wake()

    def getCurrentPowerMonitorCurrentOverflow(self):
        """ Returns true if the sensor has detect current overflow. In
        this case the current and power values are invalid."""
        self.createCurrentPowerMonitor()
        return self.currentPowerMonitor.current_overflow()
    
    def currentPowerMonitorReset(self):
        """ Reset the INA219 to its default configuration. """
        self.createCurrentPowerMonitor()
        return self.currentPowerMonitor.reset()

if __name__ == "__main__":
    tex = TexInterface()
    tex.helloWorld()
    

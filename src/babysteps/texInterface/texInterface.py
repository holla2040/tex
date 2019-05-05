#!/usr/bin/env python3

from temperatureSensor import TemperatureSensor
import RPi.GPIO as gpio

class TexInterface():

    tempSensorAddress = 0x4C
    ledPinRed = 9
    ledPinGreen = 11
    ledPinBlue = 8
    
    def __init__(self):
        self.tempSensor = None
        gpio.setmode(gpio.BCM)
        #gpio.setup(TexInterface.ledPinRed, gpio.OUT)
        #gpio.setup(TexInterface.ledPinGreen, gpio.OUT)
        gpio.setup(TexInterface.ledPinBlue, gpio.OUT)

    def cleanup(self):
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


    if __name__ == "__main__":
        tex = TexInterface()
        tex.helloWorld()
    


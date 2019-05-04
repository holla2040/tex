#!/usr/bin/env python3

from temperatureSensor import TemperatureSensor


class TexInterface():

    tempSensorAddress = 0x4C

    def __init__(self):
        self.tempSensor = None

    def helloWorld(self):
        print("Hello world")

    def createTempSensor(self):
        if None == self.tempSensor:
            self.tempSensor = TemperatureSensor(address=TexInterface.tempSensorAddress)
    def getTempC(self):
        self.createTempSensor()
        return self.tempSensor.getTempC()
    def getTempF(self):
        self.createTempSensor()
        return self.tempSensor.getTempF()

                      

if __name__ == "__main__":
    tex = TexInterface()
    tex.helloWorld()
    


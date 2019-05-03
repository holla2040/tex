#!/usr/bin/env python3

from temperatureSensor import TemperatureSensor

class TexInterface():

    def __init__(self):
        self.temperatureSensor = None

    def helloWorld(self):
        print("Hello world")

    def getTempF(self):

    def getTempC(self):
        if None == self.temperatureSensor:
                      

if __name__ == "__main__":
    tex = TexInterface()
    tex.helloWorld()
    


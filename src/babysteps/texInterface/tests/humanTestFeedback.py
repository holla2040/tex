#!/usr/bin/env python3

import sys
import os

(filePath, fileName) = os.path.split(__file__)
sys.path.insert(0,os.path.join(filePath, "../lib"))

from lib_oled96 import ssd1306
from smbus import SMBus
import RPi.GPIO as gpio
import time

class HumanTestFeedback():

    button1 = 22
    button2 = 10
    
    def __init__(self, waitForResponseSecs = 15, debug = False):
        self.waitForResponseSecs = waitForResponseSecs
        self.debug = debug
        self.i2cbus = SMBus(1)
        self.oled = ssd1306(self.i2cbus)   
        self.button1Pressed = False
        self.button2Pressed = False
        gpio.setmode(gpio.BCM)
        gpio.setup(HumanTestFeedback.button1, gpio.IN, pull_up_down=gpio.PUD_UP)
        gpio.setup(HumanTestFeedback.button2, gpio.IN, pull_up_down=gpio.PUD_UP)
        gpio.add_event_detect(HumanTestFeedback.button1,gpio.FALLING,callback = self.buttonEvent,bouncetime=300)
        gpio.add_event_detect(HumanTestFeedback.button2,gpio.FALLING,callback = self.buttonEvent,bouncetime=300)
        self.oled.cls()
        
    def buttonEvent(self, channel):
        self.button1Pressed
        self.button2Pressed
        if channel == HumanTestFeedback.button1:
            self.button1Pressed = True
            if self.debug:
                print ('button1Pressed = True')
        elif channel == HumanTestFeedback.button2:
            self.button2Pressed = True
            if self.debug:
                print ('button2Pressed = True')

    def printMsgToScreen(self, message):
        xPos = 1
        yPos = 0
        self.oled.cls()
        #self.oled.canvas.rectangle((0, 0, self.oled.width-1, self.oled.height-1), outline=1, fill=0)
        if self.debug and len(message) > 2:
            print (('WARNING: length of argument messageArray >4 lines. '
           'Only first 4 lines will be printed'))
        for line in message [0:2]:
            self.oled.canvas.text((xPos,yPos), line, fill=1)
            yPos += 15
        self.oled.canvas.text((xPos,30), 'Push Button:', fill=1)
        self.oled.canvas.text((76,30), 'yes   no', fill=1)
        self.oled.canvas.text((77,45), '\/    \/', fill=1)
        self.oled.display()
        
    def msgToScreenGetResponse(self, message):
        self.printMsgToScreen(message)
        response = None
        #Button1 = yes Button2 = no
        while True:            
            if self.button1Pressed: #yes
                self.button1Pressed = False
                response = True
                break
            elif self.button2Pressed: #no
                self.button2Pressed = False
                response = False
                break
            time.sleep(.01)
        self.oled.cls()
        return response
    
    def __del__ (self):
       self.oled.cls()
       gpio.cleanup()

if __name__ == "__main__":
    humanTestFeedback = HumanTestFeedback()
    try:
        message = ["hello world"]
        response = humanTestFeedback.msgToScreenGetResponse(message)
        if response:
            print ('yes')
        else:
            print ('no')
    except KeyboardInterrupt:
        pass
    humanTestFeedback.__del__()
    
    

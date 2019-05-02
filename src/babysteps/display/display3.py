#!/usr/bin/env python
from lib_oled96 import ssd1306
from smbus import SMBus
import RPi.GPIO as gpio
import time

i2cbus = SMBus(1)        
oled = ssd1306(i2cbus)   
switch1 = 22
switch2 = 10

def setup ():
    gpio.setmode(gpio.BCM)
    gpio.setup(switch1, gpio.IN)
    gpio.setup(switch2, gpio.IN)

def loop ():
    while True:
        if gpio.input (switch1)==gpio.LOW:
            oled.cls()
            oled.canvas.text((20,15), "Button 1 pressed!", fill=1)
            time.sleep(.25)
        elif gpio.input (switch2)==gpio.LOW:
            oled.cls()
            oled.canvas.text((20,15), "Button 2 pressed!", fill=1)
            time.sleep(.25)
        else:
            oled.canvas.rectangle((0, 0, oled.width-1, oled.height-1), outline=1, fill=0)
            oled.canvas.text((15,15), "No buttons pressed", fill=1)
        oled.display()
        time.sleep(.01)
                
def destroy ():
    oled.cls()
    gpio.cleanup()

if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()




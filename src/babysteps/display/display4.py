#!/usr/bin/env python
from lib_oled96 import ssd1306
from smbus import SMBus
import RPi.GPIO as gpio
import time

i2cbus = SMBus(1)        
oled = ssd1306(i2cbus)   
switch1 = 22
switch2 = 10
button1Pressed = False
button2Pressed = False
screenMessage = ""

def buttonEvent(channel):
    global button1Pressed
    global button2Pressed
    if channel == switch1:
        button1Pressed = True
        print ('button1Pressed = True')
    elif channel == switch2:
        button2Pressed = True
        print ('button2Pressed = True')

def setup ():
    print ("Program is starting...")
    gpio.setmode(gpio.BCM)
    gpio.setup(switch1, gpio.IN, pull_up_down=gpio.PUD_UP)
    gpio.setup(switch2, gpio.IN, pull_up_down=gpio.PUD_UP)
    gpio.add_event_detect(switch1,gpio.FALLING,callback = buttonEvent,bouncetime=300)
    gpio.add_event_detect(switch2,gpio.FALLING,callback = buttonEvent,bouncetime=300)
    oled.cls()
    oled.canvas.text((10,15), "Setting up", fill=1)
    oled.display()
    print ("Startup is finished")
    print ("---------------")


def loop ():
    global button1Pressed
    global button2Pressed 
    
    while True:
        if button1Pressed:
            button1Pressed = False
            screenMessage = "Button 1 is pressed"
            print (screenMessage)
            oled.cls()
            oled.canvas.text((10,15), screenMessage, fill=1)
        if button2Pressed:
            button2Pressed = False
            screenMessage = "Button 2 is pressed"
            print (screenMessage)    
            oled.cls()
            oled.canvas.text((10,15), screenMessage, fill=1)
        oled.display()
        time.sleep(.001)
    
def destroy ():
    oled.cls()
    gpio.cleanup()

if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()




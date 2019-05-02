#!/usr/bin/env python
from lib_oled96 import ssd1306
from smbus import SMBus
import RPi.GPIO as gpio
import time
import sys
from ina219 import INA219
from ina219 import DeviceRangeError
import LM75

i2cbus = SMBus(1)        
oled = ssd1306(i2cbus)   
switch1 = 22
switch2 = 10
button1Pressed = False
button2Pressed = False
SHUNT_OHMS = 0.15
ina = INA219(SHUNT_OHMS)
ina.configure()
tempSensor = LM75(address=0x4C)

def buttonEvent(channel):
    global button1Pressed
    global button2Pressed
    if channel == switch1:
        button1Pressed = True
        print ('button1Pressed = True')
    elif channel == switch2:
        button2Pressed = True
        print ('button2Pressed = True')

def printToScreen(messageArray):
    xPos = 0
    yPos = 0
    oled.cls()
    oled.canvas.rectangle((0, 0, oled.width-1, oled.height-1), outline=1, fill=0)
    if len(messageArray) > 4:
        print (('WARNING: length of argument messageArray >4 lines. '
               'Only first 4 lines will be printed'))
    for message in messageArray [0:4]:
        oled.canvas.text((xPos,yPos),' '+ message, fill=1)
        yPos += 15
    oled.display()

def setup ():
    print ("Program is starting...")
    gpio.setmode(gpio.BCM)
    gpio.setup(switch1, gpio.IN, pull_up_down=gpio.PUD_UP)
    gpio.setup(switch2, gpio.IN, pull_up_down=gpio.PUD_UP)
    gpio.add_event_detect(switch1,gpio.FALLING,callback = buttonEvent,bouncetime=300)
    gpio.add_event_detect(switch2,gpio.FALLING,callback = buttonEvent,bouncetime=300)
    oled.cls()
    screenMessage = ["Press Button 1 to", "display stats.", "Press Button 2 to",
                     "display temperature."]
    printToScreen(screenMessage)
    print ("Startup is finished")
    print ("---------------")


def loop ():
    global button1Pressed
    global button2Pressed 

 #   count = -1
    while True:
        if button1Pressed:
#            count+=1
            button1Pressed = False
            screenMessageArray = ['Bus Voltage:%.1fV' % (ina.voltage()),
                                  'Bus Current:%.1fmA' % ina.current(),
                                  'Power:%.1fmW' % ina.power(),
                                  'Shunt voltage:%.1fmV' % ina.shunt_voltage()]
#            count = count%len(screenMessageArray)
            printToScreen(screenMessageArray)
        if button2Pressed:
            button2Pressed = False
            screenMessage = [' ', 'Tex Temperture:',
                             tempSensor.getTemp() + 'degrees F']
            printToScreen(screenMessage)
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




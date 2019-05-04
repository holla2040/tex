#!/usr/bin/env python
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
        self.oled = ssd1306(i2cbus)   
        self.button1Pressed = False
        self.button2Pressed = False
        gpio.setmode(gpio.BCM)n
        gpio.setup(button1, gpio.IN, pull_up_down=gpio.PUD_UP)
        gpio.setup(button2, gpio.IN, pull_up_down=gpio.PUD_UP)
        gpio.add_event_detect(button1,gpio.FALLING,callback = buttonEvent,bouncetime=300)
        gpio.add_event_detect(button2,gpio.FALLING,callback = buttonEvent,bouncetime=300)
        oled.cls()
        
    def buttonEvent(channel):
        self.button1Pressed
        self.button2Pressed
        if channel == HumanTestFeedback.button1:
            self.button1Pressed = True
            if debug:
                print ('button1Pressed = True')
        elif channel == HumanTestFeedback.button2:
            self.button2Pressed = True
            if debug:
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

    def loop ():
        global button1Pressed
        global button2Pressed 
        count = -1
        screenMessageArray = [['Bus Voltage:%.1fV' % (ina.voltage()),
                               'Bus Current:%.1fmA' % ina.current(),
                               'Power:%.1fmW' % ina.power(),
                               'Shunt voltage:%.1fmV' % ina.shunt_voltage()],
                              ['', 'Flux Capacitor:', '1.21 Gigawatts ;)'],
                              [' ', 'Tex Temperture:',
                               '%.2f' %tempSensor.getTemp() + ' deg F']]
        #Button2 as a forward button and Button1 as a back button
        while True:            
            if button2Pressed:
                count+=1
                button2Pressed = False
                count = count%len(screenMessageArray)
                print (count%len(screenMessageArray))
                print ('count = %d' % count)
                printToScreen(screenMessageArray[count])
                
            elif button1Pressed:
                count2 = count
                count2-=1
                button1Pressed = False
                print (count2)
                count2 = (count2%len(screenMessageArray))
                printToScreen(screenMessageArray[count2])
                count-=1
            
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


    
    

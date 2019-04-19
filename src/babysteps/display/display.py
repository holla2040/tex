#!/usr/bin/env python
from lib_oled96 import ssd1306
from smbus import SMBus
import time

i2cbus = SMBus(1)        
oled = ssd1306(i2cbus)   

# put border around the screen:
oled.canvas.rectangle((0, 0, oled.width-1, oled.height-1), outline=1, fill=0)

# Write two lines of text.
oled.canvas.text((40,15),    'Hello', fill=1)
oled.canvas.text((40,40),    'World!', fill=1)

# now display that canvas out to the hardware
oled.display()

# time.sleep(2.0)
oled.cls()

while True:
    oled.canvas.rectangle((0, 0, oled.width-1, oled.height-1), outline=1, fill=0)
    d = time.strftime("%m/%d/%y",time.localtime(time.time()))
    t = time.strftime("%H:%M:%S",time.localtime(time.time()))
    oled.canvas.text((40,10),d, fill=1)
    oled.canvas.text((40,25),t, fill=1)
    oled.canvas.text((3,50)," TEX", fill=1)
    oled.display()
    time.sleep(1.0)

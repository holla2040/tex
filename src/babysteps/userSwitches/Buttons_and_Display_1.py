#!/usr/bin/env python
from lib_oled96 import ssd1306
from smbus import SMBus
import time
import RPi.GPIO as gpio

# for display
i2cbus = SMBus(1)
oled = ssd1306(i2cbus)

s1 = 22
s2 = 10
#display = 

gpio.setmode(gpio.BCM)
# setting the two buttons as inputs
gpio.setup(s1, gpio.IN)
gpio.setup(s2, gpio.IN)
#gpio.setup(display, gpio.OUT)

# border
oled.canvas.rectangle((0, 0, oled.width-1, oled.height-1), outline=1, fill=0)

# text
oled.canvas.text((40,40), 'This is test text', fill=1)

oled.display()
time.sleep(10.0)


#!/usr/bin/env python
import time

import RPi.GPIO as gpio

s1	 = 22
s2	 = 10

gpio.setmode(gpio.BCM)
gpio.setup(s1,   gpio.IN)
gpio.setup(s2,   gpio.IN)

while ( 1 ):
    print "%d %d"%(gpio.input(s1),gpio.input(s2))
    time.sleep(0.25)

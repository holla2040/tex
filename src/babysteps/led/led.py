#!/usr/bin/env python2.7

from smbus import SMBus
from PCA9685 import PWM
import time,sys

fPWM = 50
i2c_address = 0x60

bus = SMBus(1) 
pwm = PWM(bus, i2c_address)
pwm.setFreq(fPWM)


'''
pwm.setDuty(0, 80)
pwm.setDuty(3, 80)
pwm.setDuty(5, 80)
pwm.setDuty(6, 80)
'''

for i in range(0, 5):
    for channel in range(0,15):
        for v in range(0, 80, 2):
            pwm.setDuty(channel, v)
    for channel in range(15,0,-1):
        for v in range(80,10,-2):
            pwm.setDuty(channel, v)


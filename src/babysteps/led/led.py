#!/usr/bin/env python2.7
# Servo2.py
# Two servo motors driven by PCA9685 chip

from smbus import SMBus
from PCA9685 import PWM
import time,sys

fPWM = 50
i2c_address = 0x60 # (standard) adapt to your module
channel = 0 # adapt to your wiring
a = 8.5 # adapt to your servo
b = 2  # adapt to your servo

global pwm
bus = SMBus(1) # Raspberry Pi revision 2
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


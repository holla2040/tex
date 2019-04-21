#!/usr/bin/env python2

from smbus import SMBus
from PCA9685 import PWM
import time,sys

fPWM = 50
i2c_address = 0x60

bus = None
pwm = None

def setup():
    print ('Starting setup()...')
    global pwm
    bus = SMBus(1) 
    pwm = PWM(bus, i2c_address)
    pwm.setFreq(fPWM)
    print ('Done with setup()')


def loop():
    print ('Starting loop()...')
    global pwm
    ''' 
    # Old test code
    pwm.setDuty(0, 80)
    pwm.setDuty(3, 80)
    pwm.setDuty(5, 80)
    pwm.setDuty(6, 80)
    '''
    assert (pwm, "Found pwm = '%s'" % pwm)
    for i in range(1000):
        for channel in range(0,16):
            for v in range(0, 80, 2):
                pwm.setDuty(channel, v)
        for channel in range(15,0,-1):
            for v in range(80,10,-2):
                pwm.setDuty(channel, v)
    print ('Did loop() %i times')
    print ('Done with loop()')

def destroy():
    print ('Starting destroy()...')
    global pwm
    for channel in range(0,16): # All LEDs off
        print ('Turning channel %s off' % channel)
        pwm.setDuty(channel, 0)
    #print ('Calling GPIO.cleanup()')
    #GPIO.cleanup()
    print ('Done with destroy()')


if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        print('\nCaught KeyboardInterrupt, calling destroy()...')
        destroy()
    print('Exiting __main__ ...')


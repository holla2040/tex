#!/usr/bin/env python2

from smbus import SMBus
import Adafruit_PCA9685
import time,sys

fPWM = 50
i2c_address = 0x60

bus = None
pwm = None

def setup():
    print ('Starting setup()...')
    global pwm
    #bus = SMBus(1) 
    #pwm = PWM(bus, i2c_address)
    pwm = Adafruit_PCA9685.PCA9685(address=i2c_address)  # This takes additional arguments address and i2c
    pwm.set_pwm_freq(fPWM) #Set the PWM frequency in hertz
    print ('Done with setup()')


def loop():
    print ('Starting loop()...')
    global pwm
    # Old test code
    '''
    pwm.set_pwm(3,0,80)
    pwm.set_pwm(5,0,80)
    pwm.set_pwm(6,0,80)
    '''
    v = 0
    for channel in range (0,16):
        print ("Setting channel %s to %s" % (channel, v))
        pwm.set_pwm(channel,0,v)
        v += int(4096/16)

    response = raw_input("Hit any key to continue ")
        
    '''
    assert (pwm, "Found pwm = '%s'" % pwm)
    for i in range(1000):
        maxV = 2
        for channel in range(0,16):
            for v in range(0, maxV, 2):
                pwm.set_pwm(channel, 0, v)
        for channel in range(15,0,-1):
            for v in range(maxV,0,-2):
                pwm.set_pwm(channel, 0, v)
    print ('Did loop() %i times')
    '''
    print ('Done with loop()')

def destroy():
    print ('Starting destroy()...')
    global pwm
    for channel in range(0,16): # All LEDs off
        print ('Turning channel %s off' % channel)
        pwm.set_pwm(channel, 0, 0)
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


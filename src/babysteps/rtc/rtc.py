#!/usr/bin/env python

# ref
#   https://www.raspberrypi.org/forums/viewtopic.php?t=17597
#   https://learn.adafruit.com/adding-a-real-time-clock-to-raspberry-pi/set-rtc-time

import smbus
import time
import signal
import sys
 
bus = smbus.SMBus(1)
RTC_ADDR = 0x6f
 
ADDR_SEC    = 0x00
ADDR_MIN    = 0x01
ADDR_HOUR   = 0x02

RTCWKDAY    = 0x03
 
def signal_handler(signal, frame):
  sys.exit(0)
 
def bcd2bin(x):
  return (((x) & 0x0f) + ((x) >> 4) * 10)
 
if __name__ == "__main__":
  signal.signal(signal.SIGINT, signal_handler)
  while True:
    print "RTCWKDAY: 0x%02X"%bus.read_byte_data(RTC_ADDR, RTCWKDAY)
    print "SECONDS:  0x%02X"%bus.read_byte_data(RTC_ADDR, ADDR_SEC)
    time.sleep(0.9) # nearly 1 sec

'''
    sec = bcd2bin(bus.read_byte_data(RTC_ADDR, ADDR_SEC) & 0x7f)
    min = bcd2bin(bus.read_byte_data(RTC_ADDR, ADDR_MIN) & 0x7f)
    hour = bcd2bin(bus.read_byte_data(RTC_ADDR, ADDR_HOUR) & 0x3f)
    print "%02d:%02d:%02d" % (hour, min, sec)
'''


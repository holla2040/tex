#!/usr/bin/env python
import time


# ref
#   https://www.raspberrypi-spy.co.uk/2013/07/how-to-use-a-mcp23017-i2c-port-expander-with-the-raspberry-pi-part-2/


import smbus
import time
 
bus = smbus.SMBus(1) 
 
DEVICE = 0x20 # Device address (A0-A2)
IODIRA = 0x00 # Pin direction register
OLATA  = 0x14 # Register for outputs
GPIOA  = 0x12 # Register for inputs
 
# Set all GPA pins as outputs by setting
# all bits of IODIRA register to 0
bus.write_byte_data(DEVICE,IODIRA,0x00)
 
# Set output all 7 output bits to 0
bus.write_byte_data(DEVICE,OLATA,0)
 
while True:
    for i in range(1,17):
      # Count from 1 to 8 which in binary will count
      # from 001 to 111
      bus.write_byte_data(DEVICE,OLATA,i)
      print "%02d %s"%(i,"{0:b}".format(i))
      time.sleep(0.25)
 
# Set all bits to zero
bus.write_byte_data(DEVICE,OLATA,0)



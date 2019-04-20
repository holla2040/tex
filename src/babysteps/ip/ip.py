#!/usr/bin/env python
from lib_oled96 import ssd1306
from smbus import SMBus
import time



# https://stackoverflow.com/questions/24196932/how-can-i-get-the-ip-address-of-eth0-in-python
import socket,fcntl,struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

eth0 = get_ip_address('eth0') 
wlan0 = get_ip_address('wlan0') 

i2cbus = SMBus(1)        
oled = ssd1306(i2cbus)   

# put border around the screen:
oled.canvas.rectangle((0, 0, oled.width-1, oled.height-1), outline=1, fill=0)

# Write two lines of text.
oled.canvas.text((5,5),    'eth0', fill=1)
oled.canvas.text((5,15),    eth0, fill=1)
oled.canvas.text((5,25),   'wlan0', fill=1)
oled.canvas.text((5,35),    wlan0, fill=1)

print " eth0:",eth0
print "wlan0:",wlan0


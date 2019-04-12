#!/usr/bin/env python
import time

import RPi.GPIO as gpio

red      = 9
green    = 11
blue     = 8
interval = 0.2

gpio.setmode(gpio.BCM)
gpio.setup(red  ,gpio.OUT)
gpio.setup(green,gpio.OUT)
gpio.setup(blue, gpio.OUT)

while ( 1 ):
    gpio.output(red,gpio.HIGH)
    gpio.output(green  ,gpio.LOW)
    gpio.output(blue   ,gpio.LOW)
    time.sleep(interval);

    gpio.output(red,gpio.LOW)
    gpio.output(green  ,gpio.HIGH)
    gpio.output(blue   ,gpio.LOW)
    time.sleep(interval);

    gpio.output(red,gpio.LOW)
    gpio.output(green  ,gpio.LOW)
    gpio.output(blue   ,gpio.HIGH)
    time.sleep(interval);

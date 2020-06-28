# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 19:17:49 2020

@author: joyce
"""

# to install: pip install pyserial
import serial

# open port
usb = serial.Serial('COM12', 115200, timeout=2)

# write command
usb.write(bytes('command'))

# read information
usb.read(1)

# close port
usb.close()
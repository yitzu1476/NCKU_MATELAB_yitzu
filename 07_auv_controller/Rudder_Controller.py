# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 17:56:54 2020

@author: user
"""

import serial

class RudderController:
    def __init__(self, RCOM):
        COM_str = 'COM' + str(RCOM)
        self.usb = serial.Serial(COM_str, 115385, timeout=2)
        print('Rudder Connect to', COM_str)
    
    def SendCommand(self, command):
        for item in range(len(command)):
            self.usb.write(bytes([command[item]]))
    
    def SetTarget(self, chan, target):
        send_str = [0x84, 0, 0, 0]
        chan_str = '0x0'+str(chan)
        send_str[1] = int(chan_str, 0)
        all_bin = bin(4*target)
        bin_len = len(all_bin)
        low_bin = all_bin[bin_len-7:]
        high_bin = all_bin[0:bin_len-7]
        low_hex = hex(int(low_bin, 2))
        high_hex = hex(int(high_bin, 2))
        send_str[2] = int(low_hex, 0)
        send_str[3] = int(high_hex, 0)
        self.SendCommand(send_str)
    
    def GetPosition(self, chan):
        send_str = [0x90, 0]
        chan_str = '0x0'+str(chan)
        send_str[1] = int(chan_str, 0)
        self.SendCommand(send_str)
        x = self.usb.read(1)
        y = self.usb.read(1)
        bin_x = bin(ord(x))
        bin_y = bin(ord(y))
        if len(bin_x) == 10:
            bin_x_cut = bin_x[2:]
        else:
            bin_x_cut = bin_x[0]+bin_x[2:]
        all_bin = str(bin_y)+str(bin_x_cut)
        pos = int(all_bin[2:], 2)/4
        print('Position of channel', str(chan), ': ', pos)
        
    
    def ClosePort(self):
        self.usb.close()
        
    
    
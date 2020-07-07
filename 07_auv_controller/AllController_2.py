# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 09:39:01 2020

@author: joyce
"""

import clr
import time
dlls_UAV = clr.AddReference('UAVMotorLib')
import UAVMotorLib
import Rudder_Controller

Thruster = UAVMotorLib.Class_Thruster()

def AllControl(Trpm, Ttime, Rxang, Ryang, TCOM, RCOM):
    ThrusterCOM = 'COM'+str(TCOM)
    Thruster.OpenPort(ThrusterCOM, '9600')
    Rudder = Rudder_Controller.RudderController(RCOM)
    
    Rxang = int(Rxang)
    Ryang = int(Ryang)
    
    # Rudder X
    if Rxang > 1500:
        zero_angx = Rxang
        one_ax = 2000-int(Rxang)
        one_angx = 992 + one_ax
    
    if Rxang == 1500:
        zero_angx = Rxang
        one_angx = Rxang
    
    if Rxang < 1500:
        zero_angx = Rxang
        one_ax = int(Rxang)-992
        one_angx = 2000 - one_ax
    
    Rudder.SetTarget(0, int(zero_angx))
    Rudder.SetTarget(1, int(one_angx))
    Rudder.GetPosition(0)
    Rudder.GetPosition(1)
    
    # Rudder Y
    if Ryang > 1500:
        zero_angy = Ryang
        one_ay = 2000-int(Ryang)
        one_angy = 992 + one_ay
    
    if Ryang == 1500:
        zero_angy = Ryang
        one_angy = Ryang
    
    if Ryang < 1500:
        zero_angy = Ryang
        one_ay = int(Ryang)-992
        one_angy = 2000 - one_ay
    
    Rudder.SetTarget(2, int(zero_angy))
    Rudder.SetTarget(3, int(one_angy))
    Rudder.GetPosition(2)
    Rudder.GetPosition(3)
    
    start_time = time.time()
    now_time = time.time()
    time_lag = now_time-start_time
    
    Thruster.SpeedUp(int(Trpm), 10)
    while(time_lag < float(Ttime)):
        now_time = time.time()
        time_lag = now_time-start_time
        continue
    Thruster.Stop(True)
    
    Thruster.ClosePort()
    Rudder.ClosePort()

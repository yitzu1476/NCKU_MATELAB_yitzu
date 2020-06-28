# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 19:14:19 2020

@author: joyce
"""

# to install: pip install pythonnet
import clr
dll_AUV = clr.AddReference('UAVMotorLib')
import UAVMotorLib

Thruster = UAVMotorLib.Class_Thruster()
# open port
Thruster.OpenPort('COM9', '9600')

Thruster.SpeedUp(500, 10)
Thruster.Stop(True)

# close port
Thruster.ClosePort()
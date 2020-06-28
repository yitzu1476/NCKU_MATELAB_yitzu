# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 10:52:35 2020

@author: user
"""

import tkinter as tk

root = tk.Tk()

# top frame
topFrame = tk.Frame(root)
topFrame.pack()
thruster_b = tk.Button(topFrame, text = 'THRUSTER!', fg = 'red')
thruster_b.pack(side = tk.LEFT)
rudder_b = tk.Button(topFrame, text = 'RUDDER!', fg = 'blue')
rudder_b.pack()

# bottom frame
bottomFrame = tk.Frame(root)
bottomFrame.pack()
battery_b = tk.Button(bottomFrame, text = 'BATTERY!', fg = 'yellow')
battery_b.pack(side = tk.LEFT)
ins_b = tk.Button(bottomFrame, text = 'INS!', fg = 'green')
ins_b.pack()

root.mainloop()
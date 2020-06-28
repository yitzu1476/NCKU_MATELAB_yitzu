# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 13:40:17 2020

@author: user
"""

import tkinter as tk

def printlines(myitem):
    print('Initializing ',str(myitem),' ...')

root = tk.Tk()

rudder_img = tk.PhotoImage(file='new_r.png')
thruster_img = tk.PhotoImage(file='new_t.png')
battery_img = tk.PhotoImage(file='new_b.png')
gyro_img = tk.PhotoImage(file='new_g.png')

r_button = tk.Button(root, image=rudder_img, command=lambda: printlines('rudder'))
t_button = tk.Button(root, image=thruster_img, command=lambda: printlines('thruster'))
b_button = tk.Button(root, image=battery_img, command=lambda: printlines('battery'))
g_button = tk.Button(root, image=gyro_img, command=lambda: printlines('gyro'))
q_button = tk.Button(root, text='Quit', command=root.destroy)

r_button.grid(row=0)
t_button.grid(row=0, column=1)
b_button.grid(row=0, column=2)
g_button.grid(row=0, column=3)
q_button.grid(row=1, columnspan=4)

root.mainloop()
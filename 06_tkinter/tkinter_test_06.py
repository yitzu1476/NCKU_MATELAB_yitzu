# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 10:24:59 2020

@author: user
"""

import tkinter as tk

root = tk.Tk()

def LeftClick(event):
    print('this is Left')
    
def RightClick(event):
    print('this is Right')

my_frame = tk.Frame(root, width=400, height=400)
# Button-1 for left click, Button-2 for middle click(rowing button), Button-3 for right click 
my_frame.bind('<Button-1>', LeftClick)
my_frame.bind('<Button-3>', RightClick)
my_frame.pack()

root.mainloop()
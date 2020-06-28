# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 10:15:19 2020

@author: user
"""

import tkinter as tk

root = tk.Tk()
root2 = tk.Tk()

def PrintName():
    print('My name is Joyceeeeeeee')

def PrintName2(event):
    print('what is your name?')

button_1 = tk.Button(root, text='Print the name', command=PrintName)
button_1.pack()

button_2 = tk.Button(root2, text='print the question')
button_2.bind('<Button-1>',PrintName2)
button_2.pack()

root.mainloop()

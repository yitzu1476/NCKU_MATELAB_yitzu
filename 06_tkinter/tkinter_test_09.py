# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 15:49:54 2020

@author: user
"""

import tkinter as tk
import tkinter.messagebox

root = tk.Tk()

tkinter.messagebox.showinfo('Info box', 'Helloooooooooo')
myAns = tkinter.messagebox.askquestion('Question 1', 'Do you know me?')

if myAns == 'yes':
    print('Heyyyyyy you!')

root.mainloop()
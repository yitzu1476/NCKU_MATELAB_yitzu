# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 11:10:24 2020

@author: user
"""

import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text = 'one', bg = 'red')
label1.pack(fill = tk.X)
label2 = tk.Label(root, text = 'two', bg = 'blue')
label2.pack(side = tk.RIGHT, fill = tk.Y)

root.mainloop()
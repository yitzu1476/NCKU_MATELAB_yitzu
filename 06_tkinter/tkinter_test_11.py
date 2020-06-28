# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 16:38:09 2020

@author: user
"""

import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

ophoto = Image.open('20200318.jpg')
photo = ImageTk.PhotoImage(ophoto)

#photo = tk.PhotoImage(file='x.png')
label = tk.Label(root, image=photo)
label.pack()

root.mainloop()
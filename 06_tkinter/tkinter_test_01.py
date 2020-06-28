# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 10:08:07 2020

@author: user
"""

import tkinter as tk

# create a window
root = tk.Tk()
theLabel = tk.Label(root, text = 'heyyyyyyyyyy')
# put theLabel in the window
theLabel.pack()

# constantly display until the x buttom is pressed
root.mainloop()
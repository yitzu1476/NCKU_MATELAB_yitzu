# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 10:01:28 2020

@author: user
"""

import tkinter as tk

root = tk.Tk()

label_1 = tk.Label(root, text='User: ')
label_2 = tk.Label(root, text='Password: ')
entry_1 = tk.Entry(root)
entry_2 = tk.Entry(root)

# sticky have N W S E parameter
label_1.grid(row=0, sticky=tk.E)
label_2.grid(row=1)
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

check_box = tk.Checkbutton(root, text='keep me logged in')
check_box.grid(columnspan=2)

root.mainloop()
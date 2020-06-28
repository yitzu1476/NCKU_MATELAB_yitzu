# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 10:42:32 2020

@author: user
"""

import tkinter as tk

class NewClass:
    def __init__(self, window):
        myFrame = tk.Frame(window)
        myFrame.pack()
        
        self.button_1 = tk.Button(myFrame, text='print message', command=self.PrintMessage)
        self.button_1.grid(row=0)
        self.button_2 = tk.Button(myFrame, text='Quittttt', command=window.destroy)
        self.button_2.grid(row=1)
    
    def PrintMessage(self):
        print('Hellooooooooooooo')
        
root = tk.Tk()
toRun = NewClass(root)

root.mainloop()
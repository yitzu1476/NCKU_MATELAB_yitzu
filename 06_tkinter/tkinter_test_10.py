# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 16:04:10 2020

@author: user
"""

import tkinter as tk

def buttonClick(item):
    myCanvas.delete(item)

def testPrint():
    print('whyyyyyyyyyy')

root = tk.Tk()

myCanvas = tk.Canvas(root, width=300, height=300)
myCanvas.pack()

redline = myCanvas.create_line(0,0,300,300, fill='red')
greenline = myCanvas.create_line(300,0,0,300, fill='green')
blueline = myCanvas.create_line(0,150,300,150, fill='blue')

redButton = tk.Button(root, text='Delete red line',command=lambda:buttonClick(redline))
deleteButton = tk.Button(root, text='Delete all', command=lambda:buttonClick(tk.ALL))
testButton = tk.Button(root, text='test print', command=testPrint)


redButton.pack(side=tk.LEFT)
deleteButton.pack(side=tk.LEFT)
testButton.pack(side=tk.LEFT)

root.mainloop()
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 11:05:07 2020

@author: user
"""

import tkinter as tk

def NewFile():
    print('Create new file...')

def OpenFile():
    print('Open file...')

def Undo():
    print('Undo step...')

def RunFile():
    print('Run Run Run')

def StopFile():
    print('STOP!!!')

root = tk.Tk()

# menu
myMenu = tk.Menu(root)
root.config(menu=myMenu)

fileMenu = tk.Menu(myMenu)
editMenu = tk.Menu(myMenu)
myMenu.add_cascade(label='File', menu=fileMenu)
myMenu.add_cascade(label='Edit', menu=editMenu)

fileMenu.add_command(label='New file', command=NewFile)
fileMenu.add_command(label='Open file', command=OpenFile)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=root.destroy)
editMenu.add_command(label='Undo', command=Undo)


# toolbox
toolbox = tk.Frame(root, bg='yellow')

RunButton = tk.Button(toolbox, text='Run', command=RunFile)
RunButton.pack(side=tk.LEFT, padx=2, pady=2)
StopButton = tk.Button(toolbox, text='Stop', command=StopFile)
StopButton.pack(side=tk.LEFT, padx=2, pady=2)

toolbox.pack(side=tk.TOP, fill=tk.X)

# Status bar
status = tk.Label(root, text='The status is ...', bd=1, relief=tk.SUNKEN, anchor=tk.E)
status.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()
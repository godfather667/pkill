#!/usr/bin/python3
# pkill.py - Process Killer App
#
# Imports
from tkinter import *
import os

#define master
master = Tk()

#Set Main Title
master.title("pkill")
#
# Global Variables (distasteful)
#
global name        # Search Box Value
global last        # Last Search Box Value
global lidx        # Search Index

#
# Initializations
sv = StringVar()   # Search Variable
last = ""          # Previous 'name' is initially empty
lidx = "0.0"       # Last Index Value
#
# Functions:
#
# Callback for Search Key
def callback_find(event=None):
    global lidx
    global last
    name = sv.get()
    pos, lidx = search(name, last, lidx)
    if (len(name) >0) and (pos == "0.0") and (lidx == "0.0"):
        return False
    if pos:
        lidx = mark(pos, True)   # Mark FLAG: True Marks Line, False Unmarks line
        last = name
        return True  
#
# Callback for Process Killer
def callback_kill():
    global lidx
    name = sv.get()
    i = advpos(lidx)
    lend = i+".0"
    line = text.get(lidx, lend)
    pid = line.split()[2]
    spid = str(pid)
    bld = "kill -9 "+spid
    f = os.popen(bld)
    now = f.read()
    text.delete("1.0", END)
    loadProcess(text)
    decpos(lidx)
    text.see(lidx)   
    return True

#
# Load Process Data and Insert into Text Window
def loadProcess(text):
    global lidx
    f = os.popen('ps -ef')
    now = f.read()
    plist = now.splitlines()
    idx = 1
    for line in plist:
        info = (line[:199] + '..') if len(line) > 199 else line
        comb = str(idx)+":  "+info
        text.insert(END, comb+"\n")
        idx += 1
    return
#
# Search Function
def search(name, last, lidx):
    if name != last:
        start = 1.0
    else:
        lidx = mark(lidx, False)  # Unmark Current Line
        pos = advpos(lidx)
        pos = pos+".0"
        start = pos
        
    pos = text.search(name, start, stopindex=END)
    if not pos:
        return "1.0", "1.0"
    return str(pos), lidx
#
# Mark Current Line
def mark(lidx, mark):
    pos = str(lidx)
    idx = pos.find('.')
    base = pos[0:idx+1]
    lidx = base+"0"
    lend = base+"end"
    text.tag_add("here",lidx,lend)
    text.tag_add("back",lidx,lend)
    if mark == True:
        text.tag_delete("back")
        text.tag_config("here", background="yellow")
    else:
        text.tag_delete("here")
        text.tag_config("back", background="#ffffff")
        
    text.see(lidx)
    return lidx
#
# Advance Position Marker
def advpos(pos):
    idx = pos.find('.')
    base = pos[0:idx]
    i = int(base)
    i += 1
    base = str(i)
    return base
#
# Advance Position Marker
def decpos(pos):
    idx = pos.find('.')
    base = pos[0:idx]
    i = int(base)
    i -= 1
    if i <= 0:
        i = 1
    base = str(i)
    return base
    
master.bind('<Return>', callback_find)
    
#
# Setup Widgets:
#
#Horizontal (x) Scroll bar
xscrollbar = Scrollbar(master, orient=HORIZONTAL)
xscrollbar.pack(side=BOTTOM, fill=X)
#Vertical (y) Scroll Bar
yscrollbar = Scrollbar(master)
yscrollbar.pack(side=RIGHT, fill=Y)
#
# Setup Control Widgets

w = Label(master, text="Search Box")
w.pack()
#e = Entry(master, textvariable=sv, vaidate="focusout", validatecommand=callback)e 
e = Entry(master, textvariable=sv)
e.pack(side=TOP)

frame = Frame(master)
b = Button(frame, text = "Find", command=callback_find)
b.pack(side=LEFT)
b = Button(frame, text = "Kill Process", command=callback_kill)
b.pack(side=LEFT, padx=20)
b = Button(frame, text = "Quit", command=quit)
b.pack(side=LEFT, padx=10)
frame.pack(side=TOP)

#Text Widget
text = Text(master, wrap=NONE,
            xscrollcommand=xscrollbar.set,
            yscrollcommand=yscrollbar.set)
text.pack(side=TOP, anchor=W, fill=X, expand=YES)

loadProcess(text)

#Configure the scrollbars
xscrollbar.config(command=text.xview)
yscrollbar.config(command=text.yview)
#Run tkinter main loop
mainloop()



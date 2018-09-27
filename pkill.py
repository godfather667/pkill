from tkinter import *
import os
#define master
master = Tk()
#Set Main Title
master.title("pkill")
#
# Global Variables (distasteful)
#
name = ""   # Search Box Value
sv = StringVar()
lidx = "0.0"

#
# Functions:
#
# Callback for Search Key
def callback_find():
    name = sv.get()
    pos = search(name, text)
    idx = pos.find('.')
    base = pos[0:idx+1]
    lidx = base+"0"
    lend = base+"end"
    text.tag_add("here",lidx,lend)
    text.tag_config("here", background="#e0e0e0")
    text.see(lidx)
    return True
#
#        self.text.tag_configure("odd", background="#ffffff")
#
#
# Callback for Process Killer
def callback_kill():
    name = sv.get()
    print(name)
    return True
#
# Load Process Data and Insert into Text Window
def loadProcess(text):
    f = os.popen('ps -ef')
    now = f.read()
    plist = now.splitlines()

    idx = 1
    for line in plist:
        info = (line[:199] + '..') if len(line) > 199 else line
        comb = str(idx)+":  "+info
        print(comb)
        text.insert(END, comb+"\n")
        idx += 1
    return
#
# Search Function
def search(name, text):
    start=1.0
    pos = text.search(name, start, stopindex=END)
    if not pos:
        return -1.0
    return pos
    


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



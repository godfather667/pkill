from tkinter import *
import os
#define master
master = Tk()
master.title("pkill")

#Horizontal (x) Scroll bar
xscrollbar = Scrollbar(master, orient=HORIZONTAL)
xscrollbar.pack(side=BOTTOM, fill=X)
#Vertical (y) Scroll Bar
yscrollbar = Scrollbar(master)
yscrollbar.pack(side=RIGHT, fill=Y)
#get data
f = os.popen('ps -ef')
now = f.read()
plist = now.splitlines()
# Control Widgets

sv = StringVar()
def callback():
    name = sv.get()
    print(name)
    return True

w = Label(master, text="Search Box")
w.pack()
#e = Entry(master, textvariable=sv, vaidate="focusout", validatecommand=callback)e 
e = Entry(master, textvariable=sv)
e.pack(side=TOP)

frame = Frame(master)
b = Button(frame, text = "Find", command=callback)
b.pack(side=LEFT)
b = Button(frame, text = "Kill Process", command=callback)
b.pack(side=LEFT, padx=20)
b = Button(frame, text = "Quit", command=quit)
b.pack(side=LEFT, padx=10)
frame.pack(side=TOP)

#Text Widget
text = Text(master, wrap=NONE,
            xscrollcommand=xscrollbar.set,
            yscrollcommand=yscrollbar.set)
text.pack(side=TOP, anchor=W, fill=X, expand=YES)

for line in plist:
    info = (line[:199] + '..') if len(line) > 199 else line
    text.insert(END, info+"\n")

#Configure the scrollbars
xscrollbar.config(command=text.xview)
yscrollbar.config(command=text.yview)
#Run tkinter main loop
mainloop()

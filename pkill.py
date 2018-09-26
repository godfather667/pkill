from tkinter import *
import os
#define master
master = Tk()

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


w = Label(master, text="Process Killer")
w.pack()
l = Label(master, text="Find: ")
#e = Entry(master, textvariable=sv, vaidate="focusout", validatecommand=callback)e 
e = Entry(master, textvariable=sv)
e.pack()
b = Button(master, text = "Find", command=callback)
b.pack(padx=5, pady=10, side=TOP)
b = Button(master, text = "Quit", command=quit)
b.pack(padx=5, pady=20, side=TOP)
b = Button(master, text = "Kill Process", command=callback)
b.pack(padx=5, pady=20, side=TOP)

#Text Widget
text = Text(master, wrap=NONE,
            xscrollcommand=xscrollbar.set,
            yscrollcommand=yscrollbar.set)
text.pack()

for line in plist:
    info = (line[:98] + '..') if len(line) > 98 else line
    text.insert(END, info+"\n")

#Configure the scrollbars
xscrollbar.config(command=text.xview)
yscrollbar.config(command=text.yview)
#Run tkinter main loop
mainloop()

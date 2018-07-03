#QUESTION 1

import tkinter
from tkinter import *
root = Tk()
label1=Label(root,text="hello world")
label1.pack()
def close_window():
    root.destroy()


bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)

button1=Button(bottomFrame,text="exit",fg="green",command=close_window)
button1.pack(side=BOTTOM)


root.mainloop()


#QUESTION 2
from tkinter import *
root = Tk()
def display():
    lbl.configure(text="hello everyone")
lbl=Label(root,text=" ")
lbl.pack()


topFrame=Frame(root)
topFrame.pack(side=TOP)
bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)
button1=Button(topFrame,text="display",fg="green",command=display)
button1.pack(side=TOP)
button2=Button(bottomFrame,text="exit",fg="red",command= exit)
button2.pack(side=BOTTOM)
root.mainloop()


#QUESTION 3

from tkinter import *
root = Tk()
def display():
    label.configure(text="hello everyone")
label=Label(root,text="press button to change text ")
label.pack(side=TOP)

Frame=Frame(root)
Frame.pack(side=BOTTOM)
button1=Button(Frame,text="change text",fg="green",command=display)
button1.grid(column=0,row=2)
button2=Button(Frame,text="exit",fg="red",command= exit)
button2.grid(column=1,row=2)

root.mainloop()



#QUESTION 4

from tkinter import *
def TakeInput():
    print(tb1.get())
    print(tb.get())
tk=Tk()
tb1=Entry(tk)
tb1.pack()

tb=Entry(tk)
tb.pack()

b=Button(tk,text="PrintInput",command= TakeInput)
b.pack()
tk.mainloop()

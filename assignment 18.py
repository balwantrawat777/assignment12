#QUESTION 1

from tkinter import *
import tkinter as tk
root=Tk()

n=int(input("enter total no. of element"))
d={}
for a in range(n):
    key=input("enter name:")
    value=int(input("enter phone number:"))
    d[key]=value

scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
mylist=Listbox(root,yscrollcommand=scrollbar.set)

for i in d:
    mylist.insert(END,i)

mylist.pack(side=LEFT,fill=BOTH)

scrollbar.config(command=mylist.yview)
mainloop()

#QUESTION 2
###
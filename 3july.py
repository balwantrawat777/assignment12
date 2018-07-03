"""import tkinter
m=tkinter.Tk()
m.mainloop()

import tkinter as tk
r=tk.Tk()
r.title('counting seconds')
def hello():
    print("hello")
button=tk.Button(r,text='stop',width=25,command=hello)
button.pack()
r.mainloop()
"""
from tkinter import  *
master=Tk()
w=Canvas(master,width=100,height=90)
w.pack()


canvas_height=60
canvas_width=100
y=int(canvas_height/2)
w.create_line((0,y,canvas_width,y))
mainloop()

#1.sys.exit






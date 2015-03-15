from sys import exit
from tkinter import *
from gui6 import hello

parent=Frame(None)
parent.pack()
hello(parent).pack(side=RIGHT)

Button(parent,text='attach',command=exit).pack(side=LEFT)
parent.mainloop()

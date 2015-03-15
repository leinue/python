from tkinter import *
from gui7 import helloPackage

frm=Frame()
frm.pack()
Label(frm,text='hello').pack()
part=helloPackage(frm)
part.pack(side=LEFT)
frm.mainloop()


from tkinter import *
win=Tk()
img=PhotoImage('/a.jpg')
can=Canvas(win)
can.pack(fill=BOTH)
can.create_image(2,2,image=img,anchor=NW)
win.mainloop()

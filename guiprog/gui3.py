import sys
from tkinter import *

def quit():
    print('hello,i must be going...')
    sys.exit()

root=Tk()
widget=Button(root,text='hello',command=quit)
widget.pack()
root.mainloop()

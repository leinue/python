import sys
from tkinter import *

def hello(event):
    print('press twice to exit')

def quit(event):
    print('hello')
    
widget=Button(None,text='hello')
widget.pack()
widget.bind('<Button-1>',hello)
widget.bind('<Double-1>',quit)
widget.mainloop()


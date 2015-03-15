import sys
from tkinter import *

class helloClass:
    def __init__(self):
        widget=Button(None,text='hello',command=self.quit).pack()
    def quit(self):
        print('dssdds')
        sys.exit()
        
helloClass()
mainloop()

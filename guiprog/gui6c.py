from tkinter import *
from gui6 import hello

class helloContainer(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.pack()
        self.makeWidgets()

    def makeWidgets(self):
        hello(self).pack(side=RIGHT)
        Button(self,text='attach',command=self.quit).pack(side=LEFT)

helloContainer().mainloop()

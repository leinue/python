from tkinter import *

class helloPackage:
    def __init__(self,parent=None):
        self.top=Frame(parent)
        self.top.pack()
        self.data=0
        self.makeWidgets()

    def makeWidgets(self):
        Button(self.top,text='bye',command=self.top.quit).pack(side=LEFT)
        Button(self.top,text='hye',command=self.message).pack(side=RIGHT)

    def message(self):
        print('hello')

helloPackage().top.mainloop()

from tkinter import *
from tkinter.dialog import Dialog

class OldDialogDemo(Frame):
    def __init(seklf,master=None):
        Frame.__init__(self,parent=master)
        pack.config(self)
        Button(self,text='pop1',command=self.dialog1).pack()
        Button(self,text='pop2',command=self.dialog2).pack()

    def dialog1(self):

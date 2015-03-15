from tkinter import *
class hello(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.pack()
        self.data=42
        self.make_widgets()

    def make_widgets(self):
        widget=Button(self,text='hello',command=self.message)
        widget.pack(side=LEFT)

    def message(self):
        self.data+=1
        print('hello from world %s' % self.data)

hello().mainloop()

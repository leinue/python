from tkinter import *
from tkinter.messagebox import showinfo

class myGUI(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        button=Button(self,text='press',command=self.reply)
        button.pack()
    def reply(self):
        showinfo(title='popup',message='button pressed')

mainwin=Tk()
popup=Toplevel()
Label(popup,text='attach').pack(side=LEFT)
myGUI(poup).pack(side=RIGHT)
mainwin.mainloop()

from tkinter.filedialog import askopenfilename
from tkinter.colorchooser import askcolor
from tkinter.messagebox import askquestion,showerror
from tkinter.simpledialog import askfloat
from tkinter import *
#from quitter import Quitter

demos={
    'open':askopenfilename,
    'color':askcolor,
    'query':lambda:askquestion('warning','you typed "rm *"\nConfirm?'),
    'error':lambda:showerror('error','he\'s dead,jim'),
    'imput':lambda:askfloat('entry','enter credit card number')
}

class Demo(Frame):
    def __init__(self,parent=None,**options):
        Frame.__init__(self,parent,**options)
        self.pack()
        Label(self,text="basic demos").pack()
        for (key,value) in demos.items():
            Button(self,text=key,command=value).pack(side=TOP,fill=BOTH)
        #Quitter(self).pack(side=TOP,fill=BOTH)

Demo().mainloop()

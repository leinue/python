from tkinter import *
from dialogTable import demos

class Demo(Frame):
    def __init__(self,parent=None,**options):
        Frame.__init__(self,parent,**options)
        self.pack()
        Label(self,text='radio demos').pack(side=TOP)
        self.var=StringVar()
        for key in demos:
            Radiobutton(self,text=key,command=self.onPress,variable=self.var,value=key).pack(anchor=NW)
            self.var.set(key)
            Button(self,text='state',command=self.report).pack(fill=X)

        def onPress(self):
            pick=self.var.get()
            print('you pressed',pick)
            print('result:',demos[pick]())

         def report(self):
             print(self.var.get())


Demo().mainloop()
    

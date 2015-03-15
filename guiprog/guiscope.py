from tkinter import *

class Gui:
    def handler(self,A,B):
        print(A,B)
    def makegui(self):
        X=42
        Button(text='hello',command=(lambda:self.handler(X,'spam'))).pack()

Gui().makegui()
mainloop()

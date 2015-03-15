from tkinter import *

class helloButton(Button):
    def _init__(self,parent=None,**config):
        Button.__init__(self,parent,**config)
        self.pack()
        self.config(command=self.callback)

    def callback(self):
        print('goodbye world')
        self.quit()

helloButton(text='hello').mainloop()

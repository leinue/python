from tkinter import *
from tkinter.messagebox import *

class NewMenuDemo(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.pack(expand=YES,fill=BOTH)
        self.createWidgets()
        self.master.title('toolbars and menus')
        
    def createWidgets(self):
        self.makeMenuBar()
        self.makeToolbar()
        L=Label(self,text='menu and toolbar demo')
        L.config(relief=SUNKEN,width=40,height=10,bg='white')
        L.pack(expand=YES,fill=BOTH)

    def makeToolbar(self):
        toolbar=Frame(self,cursor='hand2',relief=SUNKEN,bd=2)
        toolbar.pack(side=BOTTOM,fill=X)
        Button(toolbar,text='quit',command=self.quit).pack(side=RIGHT)
        Button(toobar,text='hello',command=self.greeting).pack(side=LEFT)

    def makeMenuBar(self):
        self.menubar=Menu(self.master)
        self.master.config(menu=self.menubar)
        self.fileMenu()
        self.editMenu()

    def fileMenu(self):
        pulldown=Menu(self.menubar)
        pulldown.add_command(label='open',command=self.notdone)
        pulldown.add_command(label='quit',command=self.quit)
        self.menubar.add_cascade(label='file',underline=0,menu=pulldown)

    def editMenu(self):
        pulldown=Menu(self.menubar)
        pulldown.add_command(label='paste',command=self.notdone)
        pulldown.add_command(label='spam',command=self.greeting)
        pulldown.add_separator()
        pulldown.add_command(label='delete',command=self.greeting)
        pulldown.entryconfig(4,state=DISABLED)
        self.menubar.add_cascade(label='edit',underline=0,menu=pulldown)

    def greeting(self):
        showinfo('freeting','Greeting')

    def notdone(self):
        showerror('not implemented','not yet available')

    def quit(self):
        if askyesno('verify quit','r u sure u want to quit?'):
            Frame.quit(self)

if __name__=='__main__':
    NewMenuDemo().mainloop()
    

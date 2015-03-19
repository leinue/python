from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class GuiMixin:
    def infobox(self,title,text,*args):
        return showinfo(title,text)

    def errorbox(self,text):
        showerror('error',text)

    def question(self,title,text,*args):
        return askyesno(title,text)
    
    def noedone(self):
        showerror('Not implemented','Option not available')

    def quit(self):
        ans=self.question('verify quit','r u want to quit')
        if ans:Frame.quit(self)
        
    def help(self):
        self.infobox('RTFM','see figure 1...')

    def selectOpenFile(self,file='',dir='.'):
        return askopenfilename(initialdir=dir,initialfile=file)
    
    def selectSaveFile(self,file='',dir='.'):
        return asksaveasfilename(initialfile=file,initialdir=dir)
    
    def clone(self,args=()):
        new=Toplevel()
        myclass=self.__class__
        myclass(new,*args)

    def spawn(self,pycmdline,wait=False):
        if not wait:
            portableLauncher(pycmdline,pycmdline)()
        else:
            System(pycmdline,pycmdline)()

    def browser(self,filename):
        new=Toplevel()
        view=ScrolledText(new,file=filename)
        view.text.config(height=30,width=85)
        view.text.config(font=('courier',10,'normal'))
        new.title('text viewer')

if __name__=='__main__':
    class TestMixin(GuiMixin,Frame):
        def __init__(self,parent=None):
            Frame.__init__(self,parent)
            self.pack()
            Button(self,text='quit',command=self.quit).pack(fill=X)
        def other(self):
            self.spawn('guimixin.py')

    TestMixin().mainloop()
    

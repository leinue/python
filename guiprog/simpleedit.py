from tkinter import *
from tkinter.simpledialog import askstring
from tkinter.filedialog import asksavefilename
from scrolledtext import ScrolledText

class SimpleEditor(ScrolledText):
    def __init__(self,parent=none,file=None):
        frm=Frame(parent)
        frm.pack(fill=X)
        Button(frm,text='save',command=self.onSave).pack(side=LEFT)
        Button(frm,text='cut',command=self.onCut).pack(side=LEFT)
        

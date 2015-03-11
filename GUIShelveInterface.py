from tkinter import *
from tkinter.messagebox import showerror
import shelve
shelveName='class-shelve'
fieldNames=('name','age','jo','pay')
def makeWidgets():
    global entries
    window=Tk()
    window.title('people shelve')
    form=Frame(window)
    form.pack()
    entries={}
    for (ix,label) in enumerate(('key',)+fieldNames):
        lab=Label(form,text=label)
        ent=Entry(form)
        lab.grid(row=ix,colum=0)
        ent.grid(row=ix,colum=1)
        entries[label]=ent
    Button(window,text="fetch",command=fetchRecord).pack(side=LEFT)
    Button(window,text="update",command=updateRecord).pack(side=LEFT)
    Button(window,text="quit",command=window.quit).pack(side=RIGHT)
    return window

def fetchRecord():
    key=entries['key'].get()
    try:
        record=db[key]
    except:
        showerror(title='error',message='no such key!')
    else:
            for field in fieldNames:
                entries[field].delete(0,END)
                entries[field].insert(0,repr(getattr(record,field)))

def updateRecord():
    key=entries['key'].get()


db=shelve.open(shelveName)
window=makeWidgets()
window.mainloop()
db.close()

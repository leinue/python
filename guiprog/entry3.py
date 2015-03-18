from tkinter import *

fields='Name','Job','Pay'

def fetch(v):
    for vv in v:
        print('input => %s ' %v.get())

def makeform(root,fields):
    form=Frame(root)
    left=Frame(form)
    rite=Frame(form)
    form.pack(fill=X)
    left.pack(side=LEFT)
    rite.pack(side=RIGHT,expand=YES,fil=X)

    v=[]
    for filed in fields:
        lab=Label(left,width=5,text=filed)
        ent=Entry(rite)
        lab.pack(side=TOP)
        ent.pack(side=TOP,fill=X)
        var=StringVar()
        ent.config(textvariable=var)
        var.set('enter here')
        v.append(var)
    return v

root=Tk()
vars=makeform(root,fields)
Button(root,text='tecth',command=(lambda:fetch(vars))).pack(side=LEFT)
root.bind('<Return>',lambda event:fetch(vars))
root.mainloop

    

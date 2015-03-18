from tkinter import *

demoModules=['demoDlg','demoCheck','demoRadio','demoScale']
ports=[]

def addComponents(root):
    for demos in demoModules:
        module=__import__(demo)
        part=module.Demo(root)
        part.config(bd=2,relief=GROOVE)
        part.pack(side=LEFT,expand=YES,fill=BOTH)
        parts.append(part)
        
def dumpState():
    for part in parts:
        print(part.__module__+':',end='   ')
        if hasattr(part,'report'):
            part.report()
        else:
                print('demo')

root=Tk()
root.title('frames')
Label(root,text='multiple frame demo',bg='white').pack()
Button(root,text='states',command=dumpState).pack(fill=X)
addComponents(root)
root.mainloop()

from tkinter import *
colors=['red','white','blue']

def gridbox(root):
    Label(root,text='grid').pack(columnspan=2)

row=1
root=Tk()
for color in colors:
    lab=Label(root,text=color,relief=RIDGE,width=25)
    ent=Entry(root,bg=color,relief=SUNKEN,width=50)
    lab.grid(row=row,column=0,sticky=NSEW)
    ent.grid(row=row,column=1,sticky=NSEW)
    root.rowconfigure(row,weight=1)
    row+=1

root.columnconfig(0,weight=1)
root.columnconfig(1,weight=1)

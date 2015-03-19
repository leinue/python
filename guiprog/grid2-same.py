from tkinter import *
from grid2 import gridbox,packbox

root=Tk()

Label(root,text='grid').pack()
frm=Frame(root,bd=5,relief=RAISED)
frm.pack(padx=5,pady=5)
gridbox(frm)

Label(root,text='pack').pack()
frm=Frame(root,bd=5,relief=RAISED)
frm.pack(padx=5,pady=5)
packbox(frm)

Button(root,text='quit',command=root.quit).pack()
mainloop()

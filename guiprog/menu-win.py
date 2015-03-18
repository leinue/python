from tkinter import *
from tkinter.messagebox import *

def notdone():
    showerror('not implemented','not yet availiable')

def makemenu(win):
    top=Menu(win)
    win.config(menu=top)
    
    file=Menu(top)
    file.add_command(label='New...',command=notdone,underline=0)
    file.add_command(label='open...',command=notdone,underline=0)
    file.add_command(label='quit',command=win.quit,underline=0)
    top.add_cascade(label='file',menu=file,underline=0)

    edit=Menu(top,tearoff=False)
    edit.add_command(label='cut',command=notdone,underline=0)
    edit.add_command(label='paste',command=notdone,underline=0)
    edit.add_separator()
    top.add_cascade(label='edit',menu=edit,underline=0)

    submenu=Menu(edit,tearoff=True)
    submenu.add_command(label='spam',command=win.quit,underline=0)
    submenu.add_command(label='eggs',command=notdone,underline=0)
    edit.add_cascade(label='stuff',menu=submenu,underline=0)
    

root=Tk()
root.title('menu_win')
makemenu(root)
msg=Label(root,text='window menu basics')
msg.pack(expand=YES,fill=BOTH)
msg.config(relief=SUNKEN,width=40,height=7,bg='beige')
root.mainloop()

from tkinter import *

def dialog():
    win=Toplevel()
    Label(win,text='hard drive reformatted').pack()
    Button(win,text='ok',command=win.quit).pack()
    win.protocol('WM_DELETE_WINDOW',win.quit)

    win.focus_set()
    win.grab_set()
    win.mainloop()
    win.destroy()
    print('dialog exit')

root=Tk()
Button(root,text='popup',command=dialog).pack()
root.mainloop()

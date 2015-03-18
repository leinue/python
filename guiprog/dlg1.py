from tkinter import *
from tkinter.messagebox import *

def callback():
    if askyesno('verify','do you really want to quit'):
        showwarning('yes','quit not yet implemented')
    else:
        showinfo('no','quit has been cancelled')

errmsg='sorry,no spam allowed'
Button(text='quit',command=callback).pack(fill=X)
Button(text='spam',command=(lambda:showerror('spam',errmsg))).pack(fill=X)

mainloop()

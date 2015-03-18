import sys
from tkinter import Toplevel,Button,Label

tkinter.NoDefaultRoot()

win1=Toplevel()
win2=Toplevel()

Button(win1,text='spam',command=sys.exit).pack()
Button(win2,text='APM',command=sys.exit).pack()

Label(text='popup').pack()
win1.mainloop()

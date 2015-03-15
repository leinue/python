import sys
from tkinter import *
widget=Button(None,text='hello widget world',command=sys.exit)
widget.pack()
Button(None,text='press',command=sys.exit).pack(side=LEFT,fill=X,expand=LEFT)
widget.mainloop()

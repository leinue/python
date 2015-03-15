import sys
from tkinter import *

widget=Button(None,text='hello',command=(lambda:print('hello') or sys.exit()))
widget.pack()
widget.mainloop()


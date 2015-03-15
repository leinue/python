from tkinter import *

def greeting():
    print('hello')

win=Frame()
win.pack()
Button(win,text='hello',command=greeting).pack(side=LEFT,anchor=N)
Label(win,text='hello container world').pack(side=TOP)
Button(win,text='Quit',command=win.quit).pack(side=RIGHT)

win.mainloop()


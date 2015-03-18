from tkinter import *

def fetch():
    print('input => %s' % ent.get())

root=Tk()
ent=Entry(root)
ent.insert(0,'type words here')
ent.pack(side=TOP,fill=X)

ent.focus()
ent.bind('<Return>',(lambda event:fetch()))
btn=Button(root,text='fetch',command=fetch)
btn.pack(side=LEFT)
root.mainloop()

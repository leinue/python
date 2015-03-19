from tkinter import *

def onCanvasClick(event):
    print('got click',event.x,event.y,event.widget)

def onObjectClick(event):
    print('got object click',event.x,event.y,event.widget,end='   ')
    print(event.widget.find_closest(event.x,event.y))
    
root=Tk()
canv=Canvas(root,width=100,height=100)
obj1=canv.create_text(50,30,text='click me one')
obj2=canv.create_text(50,70,text='click me two')

canv.bind('<Double-1>',onCanvasClick)
canv.tag_bind(obj1,'<Double-1>',onObjectClick)
canv.tag_bind(obj2,'<Double-1>',onObjectClick)
canv.pack()
root.mainloop()

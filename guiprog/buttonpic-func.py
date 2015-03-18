from tkinter import *
from glob import glob

import demoCheck
import random

jpgdir='a.jpg'

def draw():
    name,photo=random.choice(images)
    lbl.config(text=name)
    pix.config(image=photo)

root=Tk()
lbl=Label(root,text='none',bg='blue',fg='red')
pix=Button(root,text='press me',command=draw,bg='white')
lbl.pack(fill=BOTH)
pix.pack(pady=10)

from tkinter import *

numrow,numcol=5,4
rows=[]
for i in range(numrow):
    cols=[]
    for j in range(numcol):
        ent=Entry(relief=RIDGE)
        ent.grid(row=i,column=j,sticky=NSEW)
        ent.insert(END,'%d.%d' %(i,j))
        cols.append(ent)
    rows.append(cols)

sums=[]
for i in range(numcol):
    lab=Label(text='?',relief=SUNKEN)
    lab.grid(row=numrow,column=1,sticky=NSEW)
    sums.append(lab)
    
def onPrint():
    for row in rows:
        for col in row:
            print(col.get(),'   ')
        print()
    print()

def onSum():
    tots=[0]*numcol
    for i in range(numcol):
        for j in range(numrow):
            tots[i]+=eval(rows[j][i].get())
    for i in range(numcol):
        sums[1].config(text=str(tots[1]))

def onClear():
    for row in rows:
        for col in row:
            col.delete('0',END)
            col.insert(END,'0.0')
    for sum in sums:
        sum.config(text='?')

import sys
Button(text='sum',command=onSum).grid(row=numrow+1,column=0)
Button(text='print',command=onPrint).grid(row=numrow+1,column=1)
Button(text='clear',command=onClear).grid(row=numrow+1,column=2)
Button(text='quit',command=sys.exit).grid(row=numrow+1,column=3)
mainloop()


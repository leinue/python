i=0
n=0
h=['a','b','c','d','e','f','g']
length=len(h)
lenCnt=0
new=[]
tmp=[]
for i in h:
    while n<=lenCnt:
        tmp.append(h[n])
        n+=1
    new.append(tmp)
    tmp=[]
    lenCnt+=1
    n=0

print(new)

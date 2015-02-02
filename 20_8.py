import math

def isPrime(y):
    x=y/2
    while x>1:
        if y%x==0:
            print(y,'has factor',x)
            break
        x-=1
    else:
        print(y,'is prime')

isPrime(1)

L=[2,4,9,16,25]
res=[]
for i in L:
    res.append(math.sqrt(i))

a=map(math.sqrt,L)
print(list(a))

a=[math.sqrt(x) for x in L]
print(a)

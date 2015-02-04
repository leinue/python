import string
import re

a="map"
b=a.maketrans('abcdefghijklmnopqrstuvwxyz','cdefghijklmnopqrstuvwxyzab')
print (a.translate(b))

a=open('a.txt','r')
c=a.read()
b=re.findall(r'[a-zA-Z]',c)
print(''.join(b))

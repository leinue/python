import string

a="map"
b=a.maketrans('abcdefghijklmnopqrstuvwxyz','cdefghijklmnopqrstuvwxyzab')
print (a.translate(b))

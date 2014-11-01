class addClass(object):
    def __init__(self,val):
        self.value=val

    def __str__(self):
        return 'val is '+str(self.value)

    def __add__(self,p1):
        sum=self.value+p1.value
        return addClass(sum)

ac=addClass(10)
print(ac)
print('--------------------------')
sum=ac+ac
print(sum)

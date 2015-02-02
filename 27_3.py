class MyList():
    def __init__(self,wrapper):
        self.data=[]
        for x in wrapper:self.data.append(x)
    def __add__(self,other):
        return MyList(self.data+other)
    def __mul__(self,time):
        return MyList(self.data*time)
    def __getitem__(self,index):
        return self.data[index]
    def __len__(self):
        return len(self.data)
    def __getslice(self,low,high):
        return MyList(self.data[low:high])
    def __getattr__(self,name):
        return getattr(self.data,name)
    def append(self,node):
        self.data.append(node)
    def __repr__(self):
        return repr(self.data)
class MyListSub(MyList):
    calls=0
    def __init__(self,wrapper):
        self.adds=0
        MyList.__init__(self,wrapper)
    def __add__(self,other):
        MyListSub.calls=MyListSub.calls+1
        self.adds=self.adds+1
        return MyList.__add__(self,other)
    def states(self):
        return MyListSub.calls,self.calls,self.adds
x=MyList('fuck')
print(x)
x.append('shit')
print(x)
print(x[1:3])
print(len(x))
print(x*5)
print(x.sort())
print(x)
a=x+['shit']
print(a)
print('-'*100)

y=MyListSub('bitch')
x=MyListSub('foo')
a=y+['xieyang']
b=x+['shit']
print(a,b)
print(y.states())

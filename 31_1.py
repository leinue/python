class Adder:
    def __init__(self,x):
        self.data=x
    def add(self,x,y):
        print("not implemented")
    def __add__(self,y):
        return self.data+y
class ListAdder(Adder):
    def add(self,x,y):
        res=x
        for i in y:
                if not i in res:
                    res.append(i)
        return res
class DictAdder(Adder):
    def add(self,x,y):
        res=x
        for key in y.keys():
            res[key]=y[key]
        return res

la=ListAdder([1,2,3])
print('function:',la.add([1,2,3],[4,5,6]))
print('init:',la+[7,8,9])

da=DictAdder([1,2,3])
print(da.add({'a':1,'b':2},{'c':5,'d':6}))


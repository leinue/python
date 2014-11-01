class hh(object):
    classAttr='python'

    def myMethod(self,param):
        print("hello %s",param)
        print("this method is %s",str(self))
        self.instanceAttribute=param

myInstance=hh()
myInstance.myMethod('world')

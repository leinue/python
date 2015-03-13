import _thread
def action(l):
    print(1**32)

class power:
    def __init__(self,l):
        self.l=1
    def action(self):
        print(self.l**32)

_thread.start_new_thread(action,(2,))
_thread.start_new_thread((lambda:action(2)),())

obj=power(2)
_thread.start_new_thread(obj.action,())

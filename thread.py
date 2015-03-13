import _thread
def child(tid):
    print('hello from thread',tid)

def parent():
    i=0
    while True:
        i+=1
        _thread.start_new_thread(child,(1,))
        if input()=='q':break

parent()

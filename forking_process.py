import os,time
def counter(count):
    for i in range(count):
        time.sleep(1)
        print('[%s] => %s' % (os.getpid(),1)

for i in range(5):
    pid=os.fork()
    if pid !=0:
        print('process %d spawned' %pid)
    else:
        counter(5)
        os._exit(0)
              

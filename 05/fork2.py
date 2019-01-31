import os,sys 
from time import sleep

pid = os.fork()
if pid < 0 :
    print('create process failed')
elif pid == 0:
    print('子进程PID:',os.getpid())
    sys.exit('子进程退出')

else :
    sleep(1)
    while True:
        pass
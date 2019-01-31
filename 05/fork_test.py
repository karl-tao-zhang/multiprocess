import os,sys 
from time import sleep

pid = os.fork()
if pid < 0 :
    print('create process failed')
elif pid == 0:
    print('父进程pid:',os.getppid())
    sleep(2)
    print('父进程PID:',os.getppid())

else :
    sleep(1)
    print('Parent PID :',os.getpid())
    sys.exit('父进程退出')
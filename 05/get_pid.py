import os 
from time import sleep
pid = os.fork()

if pid < 0 :
    print('Create Process failed')
elif pid == 0:
    sleep(2)
    print('子进程的儿子',pid)
    print('子进程PID',os.getpid())
else:
    print('父进程的儿子',pid)
    print('父进程PID',os.getpid())
import os 
from multiprocessing import Process
import signal 

def handle(sig,frame):
    if sig ==SIGUSR1:
        print('老司机开车了')
    elif sig == SIGUSR2:
        print('车速有点快，系好安全带')
    elif sig ==SIGTSTP:
        os.kill(os.getpid(),SIGUSR1)
def handle(sig,frame):
    if sig == SIGINT:
        os.kill(os.getppid(),SIGUSR1)
    elif sig == SIGQUIT:
        os.kill(os.getppid(),SIGUSR2)
    elif sig == SIGUSR1:
        print('到站了，请下车')
        print('售票员下车')

def fun2():
    print(ls.getppid())
    signal(SIGINT,handle)
    signal(SIGQUIT,handle)
    signal(SIGUSR1,handle)
    pause()
    pause()
    pause()
pid = os.fork()
signal(SIGUSR1,setout)
signal(SIGUSR2,setout)
signal(SIGTSTP,setout)
if pid <0 :
    print('创建进程失败')
elif pid == 0:
    fun2()
else:
    pause()
    pause()
    pause()
    os.wait()


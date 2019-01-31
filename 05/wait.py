import os,sys 
from time import sleep

pid = os.fork()
if pid < 0 :
    print('create process failed')
elif pid == 0:
    sleep(3)
    print('子进程PID:',os.getpid())
    sys.exit(3)

else :
    #等待子进程退出
    pid,status = os.wait()
    print(pid,status)
    print(os.WEXITSTATUS(status))#获取退出状态
    while True:
        pass
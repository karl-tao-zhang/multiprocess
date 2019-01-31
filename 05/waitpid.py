import os,sys 
from time import sleep

pid = os.fork()
if pid < 0 :
    print('create process failed')
elif pid == 0:
    sleep(1)
    print('子进程PID:',os.getpid())
    sys.exit(3)

else :
    #等待子进程退出
    while True:
        sleep(1)
        pid,status = os.waitpid(-1,os.WNOHANG)
        print(pid,status)
        print(os.WEXITSTATUS(status))#获取退出状态
        if os.WEXITSTATUS(status):
            break 
        print('do something others')
    while True:
        pass
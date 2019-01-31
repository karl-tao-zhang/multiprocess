import signal 
from time import sleep 

signal.alarm(5)
#使用默认方法处理SIIGALRM信号
# signal.signal(signal.SIGALRM,signal.SIG_DFL)
#使用忽略的方式处理信号
signal.signal(signal.SIGALRM,signal.SIG_IGN)
#忽略crtl + c
signal.signal(signal.SIGINT,signal.SIG_IGN)
while True:
    sleep(2)
    print('waitting for alarm')

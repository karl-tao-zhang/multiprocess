from signal import *
import time 

#信号处理函数
def  handler(sig,frame):
    # print('接收到SIGALRM')
    if sig == SIGALRM:
        print('收到时钟信号')
    elif sig == SIGINT:
        print('滚回去')

alarm(5)

#信号使用handler函数处理
signal(SIGALRM,handler)
signal(SIGINT,handler)


while True:
    print('waiting for a signal')
    time.sleep(2)

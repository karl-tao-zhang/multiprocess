import signal
import time 

#3秒后向自身发送SIGALRM信号
# signal.alarm(3)
# time.sleep(4)
signal.alarm(5)
signal.pause()
while True:
    time.sleep(1)
    print('等待时钟信号......')

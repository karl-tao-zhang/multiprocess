import os 
import signal

#表示给4617发送    SIGKILL
os.kill(4617,signal.SIGKILL)
#给父进程发送信号
os.kill(os.getppid(),signal.SIGALRM)
#给子进程发信号
os.kill(p.pid,signal)
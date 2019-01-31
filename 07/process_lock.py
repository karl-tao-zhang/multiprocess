from multiprocessing import Process,Lock
import sys
from time import sleep 

#sys.stdout为共享资源，所有进程都可以操作

def writer1():
    lock.acquire()  #上锁
    for i in range(5):
        sleep(1)
        sys.stdout.write('人生苦短\n')
    lock.release()#解锁

def writer2():
    with lock:
        for i in range(5):
            sleep(1)
            sys.stdout.write('我用python\n')
    

#创建锁
lock = Lock()
w1 = Process(target = writer1)
w2 = Process(target = writer2)

w1.start()
w2.start()

w1.join()
w2.join()

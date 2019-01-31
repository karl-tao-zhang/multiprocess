from multiprocessing import Process,Event
from time import sleep 
'''
三个进程都要操作共享资源
要求必须主进程先操作
子进程中谁先操作都可以，但是有一个子进程不能长期阻塞
'''
def wait_event():
    print("想操作临界区，但是要等主进程操作完")
    e.wait()
    print("主进程操作完了，可以操作",e.is_set())

def wait_event_timeout(sec):
    print("也想操作临界区，但是要等主进程操作完")
    e.wait(sec)
    print("等不了了，不等了先执行别的",e.is_set())

e = Event()
p1 = Process(target = wait_event)
p2 = Process(target = wait_event_timeout,\
             args=(2,))

p1.start()
p2.start()

print("主进程先操作资源")
sleep(3)
print("主进程操作完毕,set")
e.set()

p1.join()
p2.join()

from multiprocessing import Process,Queue 
import time 

#创建消息队列
q = Queue()

def fun1():
    time.sleep(1)
    q.put({'1':[1,2,3,4]})
    print('收到消息',q.get())

def fun2():
    print('收到消息',q.get())
    time.slee        p(3)
    q.put({'2':[1,2,3,4]})

p1 = Process(target = fun1)
p2 = Process(target = fun2)

p1.start()
p2.start()

p1.join()
p2.join()
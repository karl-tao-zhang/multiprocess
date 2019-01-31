#daemon属性
from threading import Thread
from time import sleep 

def fun():
    sleep(3)
    print("daemon测试")

t = Thread(target = fun)
t.setDaemon(True)
print(t.isDaemon())  #查看daemon 属性
t.start()
print('====main thread over ====')
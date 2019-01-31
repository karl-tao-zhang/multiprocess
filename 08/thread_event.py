import threading 
from time import sleep 
e=threading.Event()
s = None 

def bar():
    print(  '呼叫foo')
    global s 
    s = '天王盖地虎'

def foo():
    print('等待口令')
    sleep(2)
    if s == '天王盖地虎':
        print('自己人')
    else:
        print('打死他')
    e.set()

def fun():
    print('呵呵......')
    e.wait()
    sleep(1)
    global s 
    s = '小鸡炖蘑菇'

t1 = threading.Thread(target = bar)
t2 = threading.Thread(target = foo)
t3 = threading.Thread(target = fun)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
from multiprocessing import Event
#创建事件对象
e = Event()
e.set()#设置事件 
e.wait(5)
print('=====')
print(e.is_set())
e.set()
e.clear()#清楚设置
e.wait(3)
print(e.is_set())
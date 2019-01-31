from threading import Thread,currentThread 
from time import sleep 

#线程函数
def fun(sec):
    print("线程属性测试")
    sleep(sec)
    #获取线程对象
    print("%s 线程结束"%currentThread().getName())

thread = []

for i in range(3):
    t = Thread(target = fun,name = 'tedu%d'%i,\
        args = (3,))
    thread.append(t)
    t.start() 
    print(t.is_alive())#查看进程状态
thread[1].setName('Tarena')#设置线程名称
print(thread[2].name)#获取线程名称
#回收线程
for i in thread:
    i.join()
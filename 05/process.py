import multiprocessing as mp 
from time import sleep 
import os 
a=1
#进程事件
def fun():
    # print('哈哈哈哈 我就是这么强大a=',a)

    global a 
    a = 10000
    print('a=',a)
    
    sleep(3)
    print('你他吗个傻逼')

#创建进程对象
p = mp.Process(target = fun)

#启动进程
p.start()
sleep(2)
print('傻逼儿子 草拟吗')
#回收进程
# p.join()
while True:
    pass
print('*********')
# print(a)
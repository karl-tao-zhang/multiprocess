from multiprocessing import Process 
from time import sleep 

def worker(sec,name):
    for i in range(3):
        sleep(sec)

        print("I'm %s"%name)
        print("I'm working....")
#通过args给函数传参
#通过kwargs给函数传参
p = Process(name = 'Worker',target = worker,args = (2,'Levi'))
# names = ['Adanm','Eve','James']
p.start()
#判断进程状态
print('is alive?>',p.is_alive())
#进程名
print('process name:',p.name)
#子进程PId
print('process PID :',p.pid)
p.join()
print('*********Process over')
# print('is alive?>',p.is_alive())
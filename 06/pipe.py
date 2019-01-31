from multiprocessing import Process,Pipe
import os,time

#创建管道
fd2,fd1 = Pipe(False)

def fun(name):
    time.sleep(3)
    #向管道写入内容
    fd1.send("hello" + str(name)) #传什么都可以

jobs = []
for i in range(5):
    p = Process(target = fun,args = (i,))
    jobs.append(p)
    p.start()

for i in range(5):
    #读取管道
    data = fd2.recv()
    print(data)


for i in jobs:
    i.join()
from threading import Thread 
from time import ctime,sleep

#创建自己的线程类
class MyThread(Thread):
    def __init__(self,target,name = 'Tedu',\
        args =(),kwargs = {}) :
        super().__init__()
        self.name = name 
        self.target = target 
        self.args = args 
        self.kwargs = kwargs 

    def run(self):
        self.target(*self.args,**self.kwargs)


#线程事件
def player(song,sec):
    for i in range(2):
        print('Playing %s:%s'%(song,ctime()))
        sleep(sec)

t = MyThread(target = player,args = ('凉凉',3))
t.start()
t.join()
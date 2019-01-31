#创建二级子进程
import os 
from time import sleep 

def fun1():
    sleep(3)
    print('第一件事情')

def fun2():
    sleep(4)
    print('第二件事')

pid = os.fork() 

if pid < 0 :
    print('Create process error')
elif pid ==0:
    #创建完二级进程马上退出
    pid0 = os.fork()
    if pid0 < 0 :
        print('创建二级进程失败')
    elif pid0 ==0:
        fun2()  #做第二件事
    else:
        os._exit(0)
else:
    os.wait()
    fun1() #做第一件事
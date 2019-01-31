import os 
from time import sleep
print('===============')
a = 1
pid = os.fork()
if pid < 0 :
    print('创建进程失败')
elif pid == 0:
    sleep(1)
    print('a=',a)
    a = 10000
    print('子进程a=',a)
    print('新创建的进程')
else:
    print('父进程a=',a)
    sleep(2)  #让出内存资源让子进程先执行
    print('原来的进程')

print('程序执行完毕')
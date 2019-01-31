from  multiprocessing import Value,Process
import time 
import random 

#创建共享内存对象
#存放整形，初始值为2000
money = Value('i',2000)

#存钱
def deposite():
    for i in range(100):
        time.sleep(0.05)
        #对money value属性进行操作
        money.value += random.randint(1,200)
        print(money.value)
#取钱
def withdraw():
    for i in range(100):
        time.sleep(0.04)
        money.value -= random.randint(1,200)
        print(money.value)

d = Process(target = deposite)
w = Process(target = withdraw)

d.start()
w.start()

d.join()
w.join()

print(money.value)

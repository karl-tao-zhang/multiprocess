from multiprocessing import Pool 
import time 

def fun(n):
    time.sleep(1)
    print('执行pool map事件')
    return n*n 

#创建进程池对象
pool = Pool(4)
#使用map将事件放入进程池
r = pool.map(fun,range(6))
print('返回值列表r',r)
pool.close()
pool.join()
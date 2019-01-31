from multiprocessing import Process 
import time 

class ClockProcess(Process):
    def __init__(self,value):
        #调用父类的__init__
        super().__init__()
        self.value = value 

    #重写run方法
    def run(self):
        for i in range(3):
            time.sleep(self.value)
            print('The time is {}'.\
                format(time.ctime()))

#用自己的类创建进程对象
p = ClockProcess(10)
#自动执行run
'''
def start(self):
    self.run()
'''
p.start()
p.join()
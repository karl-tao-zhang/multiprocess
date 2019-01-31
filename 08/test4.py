from test import * 
import threading  
import time 

counts = []

t = time.time()
for x in range(10):
    th  = threading.Thread(target = count,\
           args = (1,1))
    counts.append(th)
    th.start()
    
for i in counts:
    i.join() 

print('Thread cpu:',time.time() - t)
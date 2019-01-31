from test import * 
import threading  
import time 
import multiprocessing
counts = []

def io():
    write()
    read()

t = time.time()
for x in range(10):
    p  = multiprocessing.Process(target =io)
    counts.append(p)
    p.start()
    
for i in counts:
    i.join() 

print('Process IO:',time.time() - t)

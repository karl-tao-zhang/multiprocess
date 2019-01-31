# test1.py
from test import *
import time 
t = time.time()
# for i in range(10):
#     count(1,1)
# print("Line cpu:",time.time() - t)
for i in range(10):
    write()
    read()
print("LINE IO",time.time() - t)
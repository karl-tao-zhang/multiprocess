import os 
import sys

# os._exit(9)
# print('Process end')

try:
    sys.exit('进程退出')
except SystemExit as e:
    print(e)
    

print('Process end')
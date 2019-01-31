import multiprocessing as mp 
from signal import * 
import os,sys 
import time 

def driver_handle(sig,frame):
    if sig == SIGUSR1:
        print('老司机开车了')
    elif sig == SIGUSR2:
        print('车速有点快，系好安全带')
    elif sig == SIGTSTP:
        os.kill(p.pid,SIGUSR1)

def saler_handle(sig,frame):
    if sig == SIGINT:
        os.kill(os.getppid(),SIGUSR1)
    elif sig == SIGQUIT:
        os.kill(os.getppid(),SIGUSR2)
    elif sig == SIGSUR1:
        print('停车，我要下车')
        sys.exit('我也下车')

def saler():
    signal(SIGUSR1,driver_handle)
    signal(SIGINT,driver_handle)
    signal(SIGQUIT,driver_handle)
    signal(SIGTSTP,SIG_IGN)
    while True:
        time.sleep(1)
        print('caonima nigedashabi')

p = mp.Process(target = saler)

p.start()
signal(SIGUSR1,driver_handle)
signal(SIGUSR2,driver_handle)
signal(SIGTSTP,driver_handle)
signal(SIGINT,SIG_IGN)
signal(SIGQUIT,SIG_IGN)

p.join()

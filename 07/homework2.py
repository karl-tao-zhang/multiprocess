import multiprocessing as mp 
from signal import *
import sys,os 
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
    elif sig == SIGUSR1:
        print("到站了，请下车")
        sys.exit("售票员下车")

def saler():
    signal(SIGINT,saler_handle)
    signal(SIGQUIT,saler_handle)
    signal(SIGUSR1,saler_handle)
    signal(SIGTSTP,SIG_IGN)
    while True:
        time.sleep(3)
        print('hahahaha我就是这么强大')

p = mp.Process(target = saler)
p.start()

signal(SIGUSR1,driver_handle)
signal(SIGUSR2,driver_handle)
signal(SIGTSTP,driver_handle)
signal(SIGINT,SIG_IGN)
signal(SIGQUIT,SIG_IGN)

p.join()
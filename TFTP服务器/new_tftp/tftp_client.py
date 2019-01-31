from socket import * 
import sys 
import time 

#功能封装为类
class TftpClient(object):
    def __init__(self):
        pass 
    def do_list(self):
        pass 
    def do_get(self):
        pass
    def do_put(self):
        pass 
    def do_quit(self):
        pass  

#套接字连接服务器
def main():
    if len(sys.argv) <3:
        print('argv is error')
        return 
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)

    s = socket()
    s.connect(addr)

    while True:
        print('')
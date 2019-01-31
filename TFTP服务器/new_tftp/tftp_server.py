from socket import * 
import os 
import signal 
import sys
import time 

#文件库
FILE_PATH = "/home/tarena/"

#服务器功能
class TftpServer(object):
    def __init__(self,connfd):
        self.connfd = connfd
    def handler():
        while True:
            data = self.connfd.recv(1024)
            if data == 'list':
                self.do_list()
            elif data == 'get':
                self.do_get()
            elif data == 'put':
                self.do_put()
            elif data =='quit':
                print(self.connfd.getpeername,'客户端退出')
                self.connfd.close()
                sys.exit(0)


    def do_list(self):
        pass
    def do_get(self):
        pass 
    def do_put(self):
        pass 




#控制程序流程　创建套接字，接收连接，创建子进程
def main():
    HOST = '0.0.0.0'
    PORT = 8888
    ADDR = (HOST,PORT)

    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)

    print('Listen to port 8888 ...')
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    while True:
        try:
            connfd,addr = s.accept()
        except KeyboardInterrupt:
            s.close()
            sys.exit("退出服务器")
        except Exception as e :
            print(e)
            continue 
        print('客户端登录',addr)

        #创建子进程
        pid = os.fork()
        if pid < 0 :
            print('create process failed')
            connfd.close()
            continue
        elif pid ==0:
            s.close()
            tftp = TftpServer(connfd)
            tftp.handler()

        else:
            connfd.close()
            continue 

if __name__ == '__main__':
    main()
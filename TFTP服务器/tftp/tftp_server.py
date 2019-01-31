from socket import *
import os,sys
import signal
import time

# 文件库位置
FILE_PATH = "/home/tarena/aid1803/pythonweb/day03/"


class TftpServer(object):
    def __init__(self,connfd):
        self.connfd = connfd



    def do_list(self):
        filelist = os.listdir(FILE_PATH)
        if not filelist:
            self.sonnfd.send(b'N')
            return
        else:
            self.sonnfd.send(b'Y')
        time.sleep(0.1)
        files = ''
        for filename in filelist:
            if filename[0] != '.' and os.path.isfile(FILE_PATH + filename):
                files = files + iflename + '#'

        self.connfd.send(files.encode())


    def do_get(self,filenna):
        try:
            fd = open(FILE_PATH + filename,'rb')
        except:
            self.connfd.send(b'N')
            return
        self.connfd.send(b'Y')
        time.sleep(0.1)
        while True:
            date = fd.read(1024)
            if not data:
                time.sleep(0.1)
                self.connfd.send(b'##')
                break
                self.connfd.send(n'##')
        fd.close()
        print("发送文件成功")


    def do_put(self):
        pass
    # def do_quit(self):
    #     pass


def main():
    if len(sys.argv) < 3:
        print("argv is error")
        sys.exit(1)
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST, PORT)
    BUFFERSIZE = 1024

    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(ADDR)
    sockfd.listen(5)
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)

    while True:
        try:
            commfd, addr = sockfd.accept()
        except KeyboardInterrupt:
            sockfd.close()
            sys.exit(0)
        except Exception:
            continue
        print("客户端登录:", addr)
        pid = os.fork()
        if pid < 0:
            print("创建子进程失败")
            connfd.close()
            continue
        elif pid == 0:
            socket.close()

            # 创建客户端通信对象
            tftp = TftpServer(connfd)

            while True:
                data = connfd.recv(BUFFERSIZE).decode()
                if data [0] == 'L':
                    tftp[.dp_list()]
                elif data[0] == 'G':
                    tftp.filename
                elif data[0] == 'P':
                    pass
                elif data[0] == 'Q':
                    print("客户端退出")
                    sys.exit(0)


        else:
            connfd.close()
            continue
if __name__ == "__main__":
    main()





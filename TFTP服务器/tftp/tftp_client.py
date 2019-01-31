from socket import *
import sys
import time


# 客户端请求类
class TftpClient(object):
    def __init__(self, sockfd):
        self.sockfd = sockfd

    def do_list(self):
        self.sockfd.send(b'L') # 发送请求类别
        data = self.sockfd.recv

        # 服务器回复 Y/N
        data = self.cosk.recv(1024).decode()
        if data == 'Y':
            data = self.sockfd.recv(4096).decode()
            files = data.splist('#')
            for file in files:
                print(file)
            print("文件列表展示完毕")
        else:
            print("请求文件列表失败")

    def do_get(self,filename):
        self.sockfd.send('G' + filename.encode())
        data = self. sockfd.recv(1024).decode()
        if data == 'Y':
            fd = open(filename,"wb")
            while True:
                data = self.sockfd.recv(1024)
                fd.write(data)
                if len(data) < 1024:
                    break

                fd.write(data)
            fd.close
            print("%s 系在完成"%filename)


        else:
            print("下载文件失败")

    def do_put(self,filename):
        try:
            fd = open(filenname,'rb')
        except:
            pring('上传的文件不存在')
            return
        self.fockfd.send(('P' + filenname).encode())
        data = self.sockfd.recv(1024).decode()
        if data == 'Y':
            while True:
                data = fdread(1024)
                if not data:
                    time.sleep(0.1)
                    self.sockfd,send(b"##")
                    break
                self.sockfd.send()

        else:
            print("上传文件失败")

    def do_quit(self):
        self.sockfd.send(b'Q')
        self.sockfd.close()
        sys.exit(0)


def main():
    if len(sys.argv) < 3:
        print("argv is error")
        sys.exit(1)
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST, PORT)
    BUFFERSIZE = 1024

    sockfd = socket()
    sockfd.connect(ADDR)

    # 创建客户请求对象
    tftp = TftpClient(sockfd)


    while True:
        print("========命令选项=========")
        print("******** list *********")
        print("******* get file ******")
        print("****** put file *******")
        print("******** quit *********")
        print("========================")
        data = input("输入命令>>>")
        if data.strip() == "list":
            tftp.do_list()

        elif data[:3] == "get":
            file = data.split(' ')[-1]
            tftp.do_get(filename)

        elif data[:3] == "put":
            file = data.split(' ')[-1]
            tftp.do_put(filename)

        elif data.strip() == "quit":
            tftp.do_quit()


        else:
            print("非法操作,请重新输入!!!")




if __name__ == "__main__":
    main()





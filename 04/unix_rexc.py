from socket import *
import os

#使用哪个文件作为套接字文件
sock_file = './sock'

#判断文件是否已经存在
if os.path.exists(sock_file):
    os.unlink(sock_file)

#创建本地套接字
sockfd = socket(AF_UNIX,SOCK_STREAM)

#绑定
sockfd.bind(sock_file)
#监听
sockfd.listen(5)

while True:
    c,addr = sockfd.accept()
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
    c.close()
sockfd.close()
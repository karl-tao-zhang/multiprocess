from socket import *

#确保通信两端用相同的套接字文件
sock_file = './sock'

#创建套接字
sockfd = socket(AF_UNIX,SOCK_STREAM)

#连接
sockfd.connect(sock_file)

while True:
    msg = input("Msg>>")
    if msg:
        sockfd.send(msg.encode())
    else:
        break
sockfd.close()
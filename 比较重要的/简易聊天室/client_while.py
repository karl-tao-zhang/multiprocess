
from socket import *
#创建套接字tcp
sockfd = socket()
#发起连接请求
sockfd.connect(('172.60.50.93',8888))

while True:
    #input
    data =input('发送>>  ')
    if not data:
        break
    #发送消息bytes格式
    sockfd.send(data.encode())
    # print('data>>  ',data)
    # print('data.encode>>  ',data.encode())
    data = sockfd.recv(1024).decode()
    print(data)
#关闭套接字
sockfd.close()
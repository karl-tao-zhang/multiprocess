# sock_server.py
from socketserver import * 

#多进程tcp并发

class Server(ForkingMixIn,TCPServer):
    pass
#处理具体请求
class Hander(StreamRequestHandler):
    def handle(self):
        #self.request相当于accept返回的套接字
        print('Connect from ', \
            self.request.getpeername())
        while True:
            data = self.request.recv(1024).decode()
            if not data :
                break
            print(data)
            self.request.send(b'Receive your message')

#生成服务器对象
server = Server(('0.0.0.0',8888),Handler)
#启动服务器
server.serve_forever()
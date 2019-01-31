# sock_server1.py
from socketserver import * 

#多进程udp并发

class Server(ForkingUDPServer):
    pass
class Handler(DatagramRequestHandler):
    def handle(self):
        #接收消息
        while True:
            data = self.rfile.readline().decode()
            if not data:
                break
            print(data)
            self.wfile.write(b'Receive message')
                

server = Server(('127.0.0.1',8888),Handler)
server.serve_forever()
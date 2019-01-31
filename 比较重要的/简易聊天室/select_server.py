from socket import * 
from select import select

#创建tcp套接字作为关注的IO
s = socket ()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('127.0.0.1',8888))
s.listen(5)

#三个关注列表
rlist = [s]
wlist = []
xlist = []
while True:
    #提交关注的IO事件，等待处理
    print("Waiting for IO ....")
    rs,ws,xs = select(rlist,wlist,xlist)
    print('rlist是',rlist)
    print('rs是',rs)


    for r in rs:
        if r is s :
            connfd,addr = r.accept()
            print('Conncet from ',addr)
            #增加关注事件
            rlist.append(connfd)
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
            else:
                print('Receive',data)
                wlist.append(r)

    for w in ws:
        w.send('这是一条回复消息'.encode())
        wlist.remove(w)

    for x in xs:
        if x is s :
            s.close()
            sys.exit(0)

    c,addr = r[0].accept()
    print('Connect from ',addr)














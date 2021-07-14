#TCP 服务器 无尽信息

import socket

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(('10.10.124.88',5000))
server.listen(128)
    #设置为监听模式，不可发送数据
    #数字为最大可连接数量

for _ in range(3):
# 尝试接受多个用户，但不能实现
# 一个断链后自动连接下一个
#后续多线程解决

#排队期间客户端发送的信息会同时一起被接受

    data=server.accept()
        #接受连接
        #data分两部分，第一部分是 对应的新socket，用于服务连接对象 ，第二部分是ip

    client=data[0]
    client.send('hello'.encode())
    print(data[1])
    while True:
        word=client.recv(1024).decode()
        #向对应socket收发数据

        print(word)

        if not word:
            break
        #防止客户强制退出

    print(data[1],'  is gone ')

    client.close()
    #断开服务结束的客户端，为下一个留出空间




server.close()
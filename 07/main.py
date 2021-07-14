#TCP 服务器

import socket

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(('10.10.124.88',5000))
server.listen(128)
    #设置为监听模式，不可发送数据
    #数字为最大可连接数量

for _ in range(4):

    data=server.accept()
    #接受连接
    #data分两部分，第一部分是 对应的新socket，用于服务连接对象 ，第二部分是ip

    client=data[0]
    client.send('hello'.encode())
    word=client.recv(1024)
    #向对应socket收发数据

    print(word.decode())
    print(data[1])

    client.close()
    #断开服务结束的客户端，为下一个留出空间




server.close()
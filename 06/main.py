#tcp 客户端

import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.bind(('10.10.124.88',8000))
#绑定端口

client.connect(('10.10.124.88',2000))
#TCP 必须先成功连接才能输入数据

#输出
for _ in range(0,3):
    word='\nhello'
    client.send(word.encode())
#TCP输出用send而非sendto

#接受
data=client.recv(1024)
print(data.decode())
##只接受数据



client.close()
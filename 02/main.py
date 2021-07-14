# UDP

import socket

client=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)

client.bind(('',5000))
#client.bind(('10.10.124.88',5000))
#不推荐写成注释里的形式，因为每个设备由多个网卡多个ip，写成注释中的话就无法保证信息接受
#绑定自身接口

#接收端
data,ip=client.recvfrom(1024)
#数字指定接受多少信息
#此步骤会阻塞  若无人发送数据则会停在这步
#获取一个元组，0是接收信息，1是对方ip和接口

word=data.decode(encoding='utf8',errors='ignore')
#默认解码方式是utf8
#默认态度是 strict————即转码失败就报错   可调节为 ignore————即转码失败则输出对应乱码



print(ip)
print(word)
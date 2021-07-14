# UDP

import socket

server = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# family表示ip类型，type表示发送信息方式是udp还是tcp
# 默认是        ipv4————socket.AF_INET     tcp————socket.SOCK_STREAM
# 也可设为      ipv6————socket.AF_INET6    udp————socket.SOCK_DGRAM
# UDP快，而且无需确认接收方是否存在
# TCP慢，但可确认接收方是否存在才发送

server.bind(('10.10.124.88', 5000))
# 绑定本身接口，若无则随机分配接口
# 注意只有一个参数，参数是元组，元组内两个参数

# 发送端
server.sendto('hello'.encode('utf8'), ('10.10.124.88', 6000))
# 需要转码才能发送
# 默认转码方式为UTF8


server.close()

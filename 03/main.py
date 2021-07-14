# 广播

import socket

radio=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

word="\nthis is hust's cast"

radio.bind(('10.10.114.140',9000))

#设置
radio.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,True)
#socket.SOL_SOCKET当前socket
#socket.SO_BROADCAST 广播属性
#true 可发送


radio.sendto(word.encode('utf8'),('255.255.255.255',5000))

radio.close()
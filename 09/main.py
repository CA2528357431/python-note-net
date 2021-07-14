import socket
import time

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
#跳过2msl等待，主动退出后 立即重复使用端口

client.bind(('10.10.124.88',6000))

client.connect(('10.10.124.88',5000))

while True:
    time.sleep(0.5)
    client.send('hello'.encode())

client.close()
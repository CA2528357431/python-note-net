#模拟浏览器
#用flask模拟一个服务器

import socket

browser=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

browser.connect(('127.0.0.1',5000))

re_line='GET/HTTP/1.1\n'
re_head='Server:gogogo\n'
re_space='\n'
re_data='gogogogogogogogogog'

re=re_line+re_head+re_space+re_data

#发送请求
browser.send(re.encode())

#接收数据
data=browser.recv(10000)

print(data.decode())






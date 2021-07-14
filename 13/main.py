# come on,服务器


import socket
import handle.deal


class server:

    def __init__(self,num):

        super().__init__()
        self.sever= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sever.bind(('', num))
        self.sever.listen(4)



    def main(self):
        while True:
            data=handle.deal.recv(self)
            client,client_data=data[0], data[1]
            address=data[2]
            if handle.deal.judge(client,client_data,address):
                target=handle.deal.get_target(client_data)
                handle.deal.convey(client, target)
            client.close()



while True:
    x = input('端口')
    if x.isalnum() and len(x)>3:
        break
    print('不可用')
print('going on')
y = int(x)
a = server(y)
a.main()
a.server.close()
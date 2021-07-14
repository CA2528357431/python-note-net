# 或许我们能让web根据需求提交页面

import socket


class server:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):

        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.server.bind(('', 8080))
        self.server.listen(128)

    def recv(self):
        while True:

            self.client, address = self.server.accept()
            # 听我的，这句话别分开写，不然会无法刷新！！！！
            # 求你别问我为什么

            self.client_data = self.client.recv(1024).decode()
            print(address, '   online')
            if not self.client_data:
                print(address, '   offline')

            else:
                self.permit()

            self.client.close()

    def permit(self):
        res_line = 'HTTP/1.1 200 OK,GOON\n'
        res_head = 'Server:caoan cool\n'
        res_space = '\n'

        dl = self.client_data.split('\n')
        line = dl[0].split(' ')
        target = line[1]
        print()
        try:
            file = open('.' + target, 'r')
            res_main = file.read()
        except Exception as er:
            res_main = 'D   O   W   N\nno such wage\n' + str(er)

        res = res_line + res_head + res_space + res_main
        self.client.send(res.encode())

    def main(self):
        self.start()
        self.recv()
        self.server.close()


a = server()
a.main()

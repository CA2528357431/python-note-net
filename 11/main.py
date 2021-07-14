# hey,见识一下服务器

import socket


class server:
    def start(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.server.bind(('10.10.114.140', 8080))
        self.server.listen(128)

    def recv(self):

        self.client = self.server.accept()[0]
        address = self.server.accept()[1]
        data = self.client.recv(1024).decode()
        print(address, '   online')
        if not data:
            print(address, '   offline')

        else:
            self.permit()

        self.client.close()

    def permit(self):
        res_line = 'HTTP/1.1 200 OK,GOON\n'
        res_head = 'Server:caoan cool\n'
        res_space = '\n'

        file = open('HTML/bata.html', 'r')
        res_main = file.read()

        res = res_line + res_head + res_space + res_main
        self.client.send(res.encode())

    def main(self):

        self.start()
        self.recv()
        self.server.close()


a = server()
a.main()

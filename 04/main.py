# UDP交流

import socket


class talk:
    def start(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client.bind(('10.10.124.88', 7000))
        self.ip = input('输入对方ip')
        if not self.ip:
            self.ip = '10.10.124.88'
        self.api = int(input('输入对方api'))
        print('linking')

    def cout(self):
        word = input('输入')
        self.client.sendto(word.encode(), (self.ip, self.api))

    def cin(self):
        data = self.client.recvfrom(1024)
        word = data[0].decode()
        print(word)


a = talk()
a.start()
while True:
    judge = int(input('1————send 2————receive 0————exit'))
    if judge == 0:
        exit()
    elif judge == 1:
        a.cout()
    elif judge == 2:
        a.cin()
    else:
        print('\nerror')

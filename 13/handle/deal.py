def recv(self):
    client,address  = self.sever.accept()
    # 别分开写！！！   这是血的教训！！
    client_data = client.recv(1024).decode()
    print(address, '   online')
    return client,client_data,address

def judge(client,client_data,address):

    if not client_data:
        print(address, '   offline')
        client.close()
        return False
    else:

        return True

def get_target(client_data):
        dl = client_data.split('\n')
        line = dl[0].split(' ')
        target = line[1]
        return target



def convey(client,target)    :
    res_line = 'HTTP/1.1 200 OK,GOON\n'
    res_head = 'Server:caoan cool\n'
    res_space = '\n'
    try:
        file = open('.'+target, 'r')
        res_main =file.read()+'\n'
    except Exception as er:
        res_main = 'D   O   W   N\nno such wage\n' + str(er)

    res = res_line + res_head + res_space + res_main
    client.send(res.encode())

    client.close()
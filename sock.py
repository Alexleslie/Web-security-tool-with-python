import socket

def dosomething():
    pass

class sock:
    def __init__(self, host, port, func):
        self.host = host
        self.port = port
        self.func = func

    def connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host, self.port))
        while True:
            recv_data = ''
            for i in range(64):
                recv_data += s.recv(1024).decode()
            print(recv_data)
            something = self.func()
            print(something)
            s.send(something.encode())


ADsock = sock(host='127.0.0.1', port=80, func=dosomething)
ADsock.connect()



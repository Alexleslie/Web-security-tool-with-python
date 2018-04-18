from socket import *

class MAIN_PROXY():
    def __init__(self):
        self.mainsocket = socket(AF_INET, SOCK_STREAM)
        self.RemoteSock = socket(AF_INET, SOCK_STREAM)

    def TargetSocket(self):
        self.RemoteSock.connect(('127.0.0.1',6666))
        self.RemoteSock.send(self.ldata)
        self.rdata = self.RemoteSock.recv(1024)
        self.Mainsock.send(self.rdata)

    def setsock(self):
        self.mainsocket.bind(('127.0.0.1',9999))
        self.mainsocket.listen(1)
        self.Mainsock,self.Mainaddr = self.mainsocket.accept()
        print('connect by ',self.Mainaddr)
        self.ldata = self.Mainsock.recv(1024)

c = MAIN_PROXY()
MAIN_PROXY()
MAIN_PROXY.setsock(c)
MAIN_PROXY.TargetSocket(c)
print('111')



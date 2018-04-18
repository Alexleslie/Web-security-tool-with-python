# -*- coding: utf-8 -*-  
import optparse
from socket import *
from threading import *


screenLock = Semaphore(value=1)



def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)   #tcp连接
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('Violent Python')
        results = connSkt.recv(100)
        screenLock.acquire()   #信号量等待
        print('[+] %d/ tcp open' % tgtPort)
        print('[+] ' + str(results))
    except:
        screenLock.acquire()
        print('[-] %d/ tcp closed' % tgtPort)
    finally:
        screenLock.release()  #信号量放行
        connSkt.close()



def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)    #由主机获取ip地址
    except:
        print('[-] Cannot resolve ', tgtHost)
        return
    try:
        tgtName = gethostbyaddr(tgtIP)  #获取物理地址
        print('[+] Scan Results for: ' + tgtName[0])
    except:
        print('[-] Scan Results for: ' + tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target=connScan,args=(tgtHost,int(tgtPort)))  #多线程
        t.start()



def main():
    parser = optparse.OptionParser('usage %prog ' + \
                    '-H <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string',
                      help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string',
                      help='specify target port')



    (options, args) = parser.parse_args()



    tgtHost = options.tgtHost
    tgtPorts = options.tgtPort.split(',')



    if ((tgtHost == None) | (tgtPorts[0] == None)):
        print('you must specify a target host and port[s]')
        exit(0)
        portScan(tgtHost, tgtPorts)



if __name__ == '__main__':
    main()

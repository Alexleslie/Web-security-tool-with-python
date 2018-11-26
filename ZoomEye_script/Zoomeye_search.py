import os
import requests
import json

host_config = {
    'app': None,
    'ver': None,
    'device': None,
    'os': None,
    'service': None,
    'ip': None,
    'hostname': None,
    'port': None,
    'country': None,
    'city': None,
}
webapp_config = {
    'app': None,
    'header': None,
    'keywords': None,
    'title': None,
    'ip': None,
    'site': None,
    'country': None,
    'city': None,
}

def saveStrToFile(file, str):
    with open(file, 'w') as output:
        output.write(str)


def config():
    print('Host Search options--->', [i for i in host_config.keys()])
    print('Web app Search options--->', [i for i in webapp_config.keys()])
    type = input('[H]ost or [W]eb app')
    if type.upper() == 'H':
        user_config = host_config.copy()
        print('Starting host search mode')
    else:
        user_config = webapp_config.copy()
        print('Starting web app search mode')
    while True:
        options = input('Selecting the search options, like port:80, service:http, ip:127.0.0.1 and ..."\n",'
                        'Enter an option one at a time, [S]top selecting the options if you like')
        if options.upper() == 'S':
            break
        else:
            try:
                key, value = options.lower().split(':')
                user_config[key] = value
            except Exception as e:
                print(e)
                print('Something error, please enter again')
                continue
    return user_config


def login():
    user = input('[-] input : username :')
    password = input('[-] input : password :')
    data = {
        'username': user,
        'password': password
    }
    data_encoded = json.dumps(data)
    try:
        r = requests.post(url='https://api.zoomeye.org/user/login', data=data_encoded)
        r_decoded = json.loads(r.text)
        access_token = r_decoded['access_token']
    except Exception as e:
        print('[-] info : username or password is wrong, please try again ')
        return None
    return access_token


def apiTest(headers, config, page=1):
    if 'ver' in config.keys():
        base_url = 'https://api.zoomeye.org/host/search?query='
    else:
        base_url = 'https://api.zoomeye.org/web/search?query='
    for key, value in config.items():
        if value is None:
            continue
        else:
            base_url += str(key)+':'+(value)
        base_url += '&'
    base_url += 'page='

    for i in range(page):
        url = base_url+str(i+1)
        print(url)
        try:
            r = requests.get(url=url, headers=headers)
            r_decoded = json.loads(r.text)
            for x in r_decoded['matches']:
                print(x['ip'])
                ip_list.add(x['ip'])
        except Exception as e:
                print('[-] info : ' + str(e))


def main():
    if not os.path.isfile(token_filename):
        print('[-] info : access_token file is not exist, please login')
        while True:
            access_token = login()
            if access_token:
                break
        saveStrToFile(token_filename, access_token)
    else:
        with open(token_filename, 'r') as f:
            access_token = f.read()

    headers = {'Authorization': 'JWT ' + access_token,}
    resoure_test = requests.get(url='https://api.zoomeye.org/resources-info', headers=headers)
    if 'expired' in resoure_test.text:
        os.remove(token_filename)
        print('Your access_token had expired, please enter the username and password')
        main()
        return
    else:
        print('Your account resourse is ', resoure_test.text)
    user_config = config()
    apiTest(headers, user_config)

    import time
    current_time = time.ctime()

    for i, j in user_config.items():
        if j is not None:
            current_time += '\n' + i + ':' + j +'\n'

    with open('Zoomeye_ip_list.txt', 'w+') as f:
        f.write(current_time)
        for i in ip_list:
            f.write(i+'\n')


if __name__ == '__main__':
    ip_list = set()
    token_filename = 'Zoomeye_access_token.txt'
    main()
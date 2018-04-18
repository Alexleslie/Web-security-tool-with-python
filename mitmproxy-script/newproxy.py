from mitmproxy import http
from mitmproxy.script import concurrent
import time
import logging

class Logger:
    def __init__(self):
        self.logger = logging.getLogger('mylogger')
        self.logger.setLevel(logging.DEBUG)

        self.fn = logging.FileHandler('text.txt')
        self.fn.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.fn.setFormatter(formatter)

        self.logger.addHandler(self.fn)

    def getlog(self, text):
        self.logger.info(text)

logger = Logger()



@concurrent
def request(flow):# request是提供给我们的方法，这里flow 代表每一个http数据包的对象的集合

    request_ob = flow.request   # 这里返回的是 HTTPRequest 这个对象

    result = 0
    main_url = request_ob.path
    #检测

    if result == 0:
        full_text = '[+] url:' + request_ob.url +\
                    '  [+] header:' + str(request_ob.headers) +\
                    '  [+] body:' + str(request_ob.content)
        logger.getlog(full_text)
       







import requests
from bs4 import BeautifulSoup
from threading import Thread

class Mythread(Thread):    # 继承thread  改写，使得其可以获得子线程的返回值
    def __init__(self,url,func):
        Thread.__init__(self)
        self.url= url
        self.func= func

    def run(self):
        self.result = self.func(self.url)

    def get_result(self):
        return self.result


class SpiderBaidu:
    def __init__(self, high ='', key='messi', pn=10):
        self.realkey = key   # 真正关键字
        self.key = "&wd=" + high + str(key)  # 带高级搜索 如 inurl 等
        self.url = 'http://www.baidu.com/s?&ie=utf-8' + self.key
        self.pn = pn  #页数、
        self.urls = []

    def get(self, url):  # 获得百度页面的请求
        try:
            r = requests.get(url,timeout=3)
            if r.status_code != 200:
                print("[-] --- PAGE_NOT_200")
                return None
            return r.text
        except:
            print('[-] --- TIME OUT')
            return None

    def parse(self,content):  # 解析页面
        if content is None:
            print("EMPTY CONTENT")
        soup = BeautifulSoup(content,'lxml')
        links = soup.find_all('a')
        urls = set()
        for i in links:  #去重
            urls.add(i.get('href'))
        for url in list(urls):
            if url is not None:
                if (self.realkey and 'http') not in url:
                    continue
                if "link?url" in url:
                    try:
                        self.urls.append(requests.get(url, timeout=5).url)  # 获得真实页面
                    except:
                        pass

    def craw(self):  #发起请求
        th = []
        for i in range(self.pn):
            print("NOW ---->开始多线程疯狂请求")
            url = self.url + "&pn=" + str(i*10)
            r = self.get(url)
            t = Thread(target=self.parse,args=(r,))
            t.start()
            th.append(t)
        for t in th:
            t.join()

    def print_url(self):
        for i in range(len(self.urls)):
            print("Craw : " + self.urls[i])
        print("[+] ---- >OK!!!!!!!")


high = 'inurl: '
key = 'php?id=1'
spider = SpiderBaidu(high, key,  20)
spider.craw()
spider.print_url()

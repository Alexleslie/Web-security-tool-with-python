import requests
import re
from urllib.parse import urlparse
from threading import Thread


def url_is_correct(url):
    try:
        requests.get(url)
        return url
    except:
        return 0

class MyThread(Thread):
    def __init__(self, func, args=()):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None


class LinkQuence:
    def __init__(self):
        self.visited = []
        self.unvisited = []


    def get_visited_url(self):
        return self.visited

    def get_unvisited_url(self):
        return self.unvisited

    def add_visited_url(self, url):
        self.visited.append(url)

    def add_unvisited_url(self, url):
        url = url_is_correct(url)
        if url and url not in self.visited and url not in self.unvisited:
            self.unvisited.append(url)

    def remove_visited(self, url):
        return self.visited.remove(url)

    def pop_unvisited_url(self):
        try:
            return self.unvisited.pop()
        except:
            return None

    def unvisited_url_empty(self):
        return len(self.unvisited) == 0


class Spider:
    def __init__(self, url):
        self.protocol = urlparse(url).scheme
        self.domain = urlparse(url).hostname
        self.LinkQuence = LinkQuence()
        self.LinkQuence.add_unvisited_url(url)
        self.current_deepth = 1

    def get_page_links(self, url):
        page_source = requests.get(url).text
        page_links = re.findall(r'(?<=href=\").*?(?=\")|(?<=href=\').*?(?=\')', page_source)
        page_links = set(page_links)
        print(url + '  the number of valid url ：' + str(len(page_links)))
        return page_links

    def process_url(self, url):
        true_url = []
        for i in self.get_page_links(url):
            if re.findall(r':', i):
                if re.findall(self.domain, i):
                    true_url.append(i)
            else:
                true_url.append(self.protocol+'://' + self.domain + i)
        print('catching this url right now', url)

        visited_url = set(true_url) & set(self.LinkQuence.visited)
        for i in visited_url:
            if i in true_url:
                true_url.remove(i)
        return true_url

    def crawler(self, crawl_deepth=1):
        th = []
        while self.current_deepth <= crawl_deepth:
            while not self.LinkQuence.unvisited_url_empty():
                visited_url = self.LinkQuence.pop_unvisited_url()
                if visited_url in self.LinkQuence.visited:
                    continue
                t = MyThread(self.process_url, args=(visited_url, ))
                t.start()
                th.append(t)
                self.LinkQuence.add_visited_url(visited_url)
            for t in th:
                t.join()
                links = t.get_result()
                for i in links:
                    self.LinkQuence.add_unvisited_url(i)
            self.current_deepth += 1
        print(len(self.LinkQuence.visited))
        return self.LinkQuence.visited


if __name__ == '__main__':
    url = 'http://www.leslie2018.com'
    spider = Spider(url)
    spider.crawler(5)



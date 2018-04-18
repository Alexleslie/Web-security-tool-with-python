from mitmproxy import http
from mitmproxy.script import concurrent
import re
from sklearn.externals import joblib

def get_len(url):
    return len(url)

def get_url_count(url):
    if re.search('(http://)|(https://)', url, re.IGNORECASE):
        return 1
    else:
        return 0

def get_evil_char(url):
    return len(re.findall("[<>,\'\"/]", url, re.IGNORECASE))

def get_evil_word(url):
    return len(re.findall("(alert)|(script=)(%3c)|(%3e)|(%20)|(onerror)|(onload)|(eval)|(src=)|"
                          "(prompt)|(union)|(and)", url, re.IGNORECASE))

def get_last_char(url):
    if re.search('/$', url, re.IGNORECASE):
        return 1
    else:
        return 0

def deal(url):
    feature = []
    f1 = get_len(url)
    f2 = get_url_count(url)
    f3 = get_evil_char(url)
    f4 = get_evil_word(url)
    feature.append([f1, f2, f3, f4])
    return feature

clf = joblib.load('xss_model.m')


@concurrent
def request(flow):
  request = flow.request
  main_url = request.path
  y_pred = clf.predict(deal(main_url))
  if y_pred == 1:
    request.path = '/danger'
    
    
    
	

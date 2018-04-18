from burp import IBurpExtender
from burp import IHttpListener
from burp import IHttpRequestResponse
from burp import IResponseInfo
from burp import IProxyListener
import re


def DealParm(parameter,cookie):   
    cookiedict = {}
    otherdict = {}
    for i in parameter:
        if i.getType() == i.PARAM_COOKIE:
            cookiedict[str(i.getName())] = str(i.getValue())
        else:
            otherdict[str(i.getName())] = str(i.getValue())
    if cookie:
        return cookiedict
    else:
        return otherdict


def CheckUrl(url_data):
    if 'order%20by' in url_data:
            return True
    else:
        return False


class BurpExtender(IBurpExtender,IHttpRequestResponse, IProxyListener):
    def registerExtenderCallbacks(self,callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        self._callbacks.setExtensionName('leslie')

        callbacks.registerProxyListener(self)

    def processProxyMessage(self, messageIsRequest, message):
        if messageIsRequest:
            request = message.getMessageInfo()
            request_after = request.getRequest()
            analyzedRequest = self._helpers.analyzeRequest(request_after)

            method = analyzedRequest.getMethod()
            headers = analyzedRequest.getHeaders()
            url = str(self._helpers.analyzeRequest(request).getUrl())
            parameter = analyzedRequest.getParameters()

            cookie = DealParm(parameter,True)
            otherPara = DealParm(parameter,False)

            print 'Cookie:',cookie
            print 'Parm:', otherPara
            print 'Headers:',headers
     

            if url:
                print 'this is the url : ', url
                if CheckUrl(url):
                    print  ' dangerous request!!!'
                    message.setInterceptAction(message.ACTION_DROP)




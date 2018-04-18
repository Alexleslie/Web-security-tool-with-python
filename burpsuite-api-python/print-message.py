from burp import IBurpExtender
from burp import IHttpListener
from burp import IHttpRequestResponse
from burp import IResponseInfo
from burp import IProxyListener


print 'this is my extender '


class BurpExtender(IBurpExtender,IHttpListener,IHttpRequestResponse, IProxyListener):
    def registerExtenderCallbacks(self,callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()



        self._callbacks.setExtensionName('leslie')



        callbacks.registerHttpListener(self)
        callbacks.registerProxyListener(self)



    def processHttpMessage(self, toolFlag, messageIsRequest, messageinfo):
        if toolFlag == 4 :
            if messageIsRequest:
                request = messageinfo.getRequest()
                analyzedRequest = self._helpers.analyzeRequest(request)
                headers = analyzedRequest.getHeaders()
                print headers

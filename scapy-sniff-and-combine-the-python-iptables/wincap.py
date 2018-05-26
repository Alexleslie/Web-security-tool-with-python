# from scapy.all import *
import threading
import time
#
# class wirecap:
#     def __init__(self, filter):
#         self.filter = filter
#         pass
#
#     def start_sniff(self):
#         sniff(filter=self.filter, method=self.method)
#
#     def method(self, packet):
#         try:
#             if packet['Raw']:
#                 data = packet['Raw']
#         except Exception as e:
#             print e

class wincap_text:
    def __init__(self):
        self.content = ''

    def start(self):
        while True:
            self.content = self.content + '-' + str(time.time())
            time.sleep(1)


class Test:
    def test(self):
        print 'run test'

    def run(self, ob):
        while True:
            second_content = ob.content
            print second_content
            ob.content = ''
            time.sleep(5)

a = wincap_text()
b = Test()
th = []

t = threading.Thread(target=a.start)
t2 = threading.Thread(target=b.run, args=(a,))
t2.start()
t.start()



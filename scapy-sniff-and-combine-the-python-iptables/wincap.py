from scapy.all import *
import threading
import time

class wirecap:
    def __init__(self, filter):
        self.filter = filter
        self.content = ''

    def start_sniff(self):
        sniff(filter=self.filter, prn=self.p_method)

    def p_method(self, packet):
        try:
            if packet['Raw']:
                data = packet['Raw'][0]
                self.content += str(data).strip('\n')
        except Exception as e:
            pass

# class wincap_text:
#     def __init__(self):
#         self.content = ''
#
#     def start(self):
#         while True:
#             self.content = self.content + '-' + str(time.time())
#             time.sleep(1)
#
#


class Test:
    def test(self):
        print 'run test'

    def run(self, ob):
        while True:
            second_content = ob.content
            if second_content=='':
                print 'content empty'
                time.sleep(1)
                continue
            print second_content
            self.write(second_content)
            ob.content = ''
            time.sleep(1)

    def write(self, data):
        with open('log.txt', 'r+') as f:
            f.write(data)


a = wirecap('tcp and (port 8080) ')
b = Test()
th = []

t = threading.Thread(target=a.start_sniff)
t2 = threading.Thread(target=b.run, args=(a,))
t2.start()
t.start()

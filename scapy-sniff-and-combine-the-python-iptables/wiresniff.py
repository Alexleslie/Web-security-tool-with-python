from scapy.all import *
import optparse


class wirecap:
    def __init__(self, method, filter_sentence, eth, count):
        self.cpt_method = self.less_data 
        self.method = method
        self.filter = filter_sentence
        self.eth = eth
        self.count = count



        if self.method != 'S' and self.method !='s':
            self.cpt_method = self.full_data



        if len(self.eth) == 0:
            self.eth = None



        try:
            self.count = int(self.count)
        except:



            self.count = None



    def full_data(self, packet):
        if packet:
            print '[+] Here is a packet!!!'
            packet.show()       
            hexdump(packet)
            print '[-] Packet end \n'



    def less_data(self, packet):
        if packet:
            print '[+] Here is a packet!!!'
            print packet.summary()
            print '[-] Packet end \n'



    def start_sniff(self):
        if self.eth:
            if self.count:
                sniff(iface=self.eth, filter=self.filter, prn=self.cpt_method, count=self.count)
            else:
                sniff(iface=self.eth, filter=self.filter, prn=self.cpt_method)



        else:
            if self.count:
                sniff(filter=self.filter, prn=self.cpt_method, count=self.count)
            else:
                sniff(filter=self.filter,prn=self.cpt_method)



def main():
    parser = optparse.OptionParser('usage%prog' + '-m <method> -f <filter> -e <eth_name> -c <count>')
    parser.add_option('-m', dest='method', type='string', default='s', help='sprcify the method [d|s]')
    parser.add_option('-f', dest='filter', type='string', default='', help='Filter the packet')
    parser.add_option('-e', dest='eth_name', type='string', default='', help='choose the eth')
    parser.add_option('-c', dest='count', type='string', default='', help='specify the number of packet')



    (options,args) = parser.parse_args()



    method = options.method
    filter_sen = options.filter
    eth = options.eth_name
    count = options.count



    cap = wirecap(method,filter_sen,eth,count)
    cap.start_sniff()



if __name__ == '__main__':
    main()

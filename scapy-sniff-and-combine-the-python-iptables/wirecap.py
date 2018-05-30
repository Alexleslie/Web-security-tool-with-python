from scapy.all import *
import iptc
codi

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

    def full_data(self, packet):        #详细模式，输出详细数据包内容
        if packet:
            print '[+] Here is a packet!!!'
            packet.show()       
            hexdump(packet)
            print '[-] Packet end \n'

    def less_data(self, packet):   #简约模式 ，输出简约数据包内容   ，且在简约模式下设置检查拦截功能
        '''
        当前分析只是http协议
        '''
        if packet:
            try:
                if packet['Raw']:    #检查是否含有 http 头内容
                    print '[+] Here is a packet!!!'
                    print packet.summary()   #打印出简略信息
                    url_data = str(packet['Raw']).split(' ')[1]   #获取http头中的url地址
                    ip_data = str(packet['IP'].src)    #获取 数据包中的源ip
                    self.check(url_data, ip_data)      #检查url是否有敏感字符
                    print '[-] Packet end \n'
            except:
                print 'do not have http header'


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


    def check(self,data,ip):       #传入url和ip
        if 'order%20by' in data:     #先实现最简单的检查
            print  '[-] * Danger'
            self.control(ip)    #调用python-iptables 设置防火墙规则


    def control(self,ip):
        print 'I have to ban this ip now !!'
        rule =iptc.Rule()      # 创建一个对象
        rule.in_interface= 'eth0'    # 设置网卡
        rule.src = ip       # 设置ip
        rule.protocol = 'tcp' # 设置协议
        chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), 'INPUT')  # 在filter表中的‘INPUT’链设置过滤规则 ，简而言之就是为输入的数据包设置规则
        rule.target = iptc.Target(rule,'DROP')  # 设置动作
        chain.insert_rule(rule)  #插入规则
        print 'this is ip can not reach my server anymore'



cap = wirecap('s','tcp and port 80','',300)  # 设置协议‘tcp’和端口为80
cap.start_sniff()
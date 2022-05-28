import re
from collections import deque
from scapy.all import bytes_hex
from scapy.utils import hexdump, linehexdump
import scapy.all as scapy

class LayerCapture:
    def __init__(self):
        self.contentsQueue = deque()

    def addContentToQueue(self,content):
        if(self.isNotBlank(content)):
            self.contentsQueue.append(content)

    def removeContentFromQueue(self):
        return self.contentsQueue.popleft()

    def getQueue(self):
        return self.contentsQueue

    def bytes_to_hex(self,bytes):
        return bytes.hex()

    def bytes_to_str(self,bytes):
        return str(bytes, 'utf-8')

    def capture_ether(self,ether_pkt):
        # print(ether_pkt.show())
        # print(ether_pkt.sprintf("{IP:%IP.src% -> %IP.dst%\n}{Raw:%Raw.load%\n}"))
        # print(ether_pkt["Raw"].load)
        dump = scapy.hexdump(ether_pkt, dump=True)
        # print(dump)

        string = ""
        start = 55
        end = start+16
        while start < len(dump):
            # print(dump[start:end])
            string = string + dump[start:end]
            start = end + 56
            end = start + 16

        print(string.replace('.',''))
        self.addContentToQueue(string.replace('.',''))

        pass

    def capture_ip(self,ip_pkt):
        print(ip_pkt.show())
        pass

    def capture_ipv6(self,ipv6_pkt):
        print(ipv6_pkt.show())
        pass

    def capture_udp(self,udp_pkt):
        hex_payload = bytes(udp_pkt.payload).hex()
        # print(hex_payload)
        self.addContentToQueue(hex_payload)
        pass

    def capture_tcp(self,tcp_pkt):
        # hexdump(tcp_pkt)
        # dump = scapy.hexdump(tcp_pkt, dump=True)
        # # print(dump)

        # string = ""
        # start = 55
        # end = start+16
        # while start < len(dump):
        #     # print(dump[start:end])
        #     string = string + dump[start:end]
        #     start = end + 56
        #     end = start + 16

        # print(string.replace('.',''))
        # print(tcp_pkt.show())
        # hh = linehexdump(tcp_pkt, dump=True)
        # hh_list = hh.replace('.','').split(' ')
        # print(linehexdump(tcp_pkt, dump=True))
        # print(hh_list[len(hh_list)-1])
        # hex_payload = bytes(tcp_pkt.payload).hex()
        # # print(hex_payload)
        # self.addContentToQueue(hex_payload)
        pass

    def capture_raw(self,raw_pkt):
        # print(raw_pkt.show())
        # print(raw_pkt.load.decode("ISO-8859-1"))
        # print(bytes_hex(raw_pkt))
        print(bytes_hex(raw_pkt))
        print(hexdump(raw_pkt))
        # try:
            # print(self.bytes_to_str(raw_pkt.load))
        # except Exception as e:
            # pass

    def capture_dns(self,dns_pkt):
        print(dns_pkt.show())
        pass

    def capture_icmp(self,icmp_pkt):
        print(icmp_pkt.show())
        pass

    def capture_arp(self,arp_pkt):
        print(arp_pkt.show())
        pass

    def capture_tls(self,tls_pkt):
        # print(tls_pkt.show())
        try:
            # print(tls_pkt.show())
            print(self.bytes_to_str(tls_pkt.data))
        except Exception as e:
            print(e)
        
        pass

    def isBlank(self,myString):
        return not (myString and myString.strip())

    def isNotBlank(self,myString):
        return bool(myString and myString.strip())
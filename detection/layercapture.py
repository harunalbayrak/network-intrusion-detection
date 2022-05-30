import re
from collections import deque
from scapy.all import bytes_hex
from scapy.utils import hexdump, linehexdump
import scapy.all as scapy

class LayerCapture:
    def __init__(self):
        self.contentsQueue = deque()

    def addContentToQueue(self,content):
        if(self.isNotBlank(content["data"])):
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

        # print(string.replace('.',''))
        data = string.replace('.','')
        ip_src=ether_pkt["IP"].src
        ip_dst=ether_pkt["IP"].dst
        port_src=ether_pkt["IP"].sport
        port_dst=ether_pkt["IP"].dport
        protocol=ether_pkt["IP"].proto
        tcp_data = ""
        udp_data = ""

        if(protocol == 6):
            tcp_data = bytes(ether_pkt["TCP"].payload).hex()
        elif(protocol == 17):
            udp_data = bytes(ether_pkt["UDP"].payload).hex()

        q = {"data":data, "tcp_data": tcp_data, "udp_data":udp_data, "ip_src":ip_src, "ip_dst":ip_dst, "port_src":port_src, "port_dst":port_dst, "protocol":protocol}
        self.addContentToQueue(q)

        # print(ether_pkt.summary())
        # print(ether_pkt.show())

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
        data = bytes(tcp_pkt.payload).hex()

        port_src=tcp_pkt.sport
        port_dst=tcp_pkt.dport

        q = {"data":data, "ip_src":0, "ip_dst":0, "port_src":port_src, "port_dst":port_dst, "protocol":6}

        self.addContentToQueue(q)

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
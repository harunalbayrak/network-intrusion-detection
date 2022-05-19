import binascii

class LayerCapture:
    def bytes_to_hex(self,bytes):
        return bytes.hex()

    def bytes_to_str(self,bytes):
        return str(bytes, 'utf-8')

    def capture_ether(self,ether_pkt):
        print(ether_pkt.show())
        pass

    def capture_ip(self,ip_pkt):
        print(ip_pkt.show())
        pass

    def capture_ipv6(self,ipv6_pkt):
        print(ipv6_pkt.show())
        pass

    def capture_udp(self,udp_pkt):
        # PacketCapture.capture_raw(udp_pkt["Raw"])
        # print(udp_pkt.show())
        # print(binascii.hexlify(str(udp_pkt.payload)))
        pass

    def capture_tcp(self,tcp_pkt):
        # PacketCapture.capture_raw(tcp_pkt["Raw"])
        # print(tcp_pkt.show())
        # print(self.bytes_to_str(tcp_pkt.payload))
        pass

    def capture_raw(self,raw_pkt):
        # print(raw_pkt.show())
        try:
            print(self.bytes_to_str(raw_pkt.load))
        except Exception as e:
            pass
        pass

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
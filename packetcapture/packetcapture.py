import os
import sys
import scapy.all as scapy
from textwrap import wrap
from scapy.layers.http import *

# Append parent directory to import path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from logger.logger import Logger
from packetcapture.layercapture import LayerCapture

class PacketCapture:
    def __init__(self,interface,layercapture):
        self.interface = interface
        self.layercapture = layercapture
        self.logger = Logger("PACKETCAPTURE")

    def analyse_packet(self,pkt):
        # self.layercapture.capture_ether(pkt["Ether"])
        # self.layercapture.capture_ip(pkt["IP"])
        # self.layercapture.capture_ipv6(pkt["IPv6"])
        # self.layercapture.capture_ipv6(pkt["Ether"])
        # self.layercapture.capture_raw(pkt["Raw"])
        # self.layercapture.capture_tls(pkt["TLS Application Data"])

        if(pkt.haslayer(scapy.UDP)):
            self.logger.print_log_info("UDP")
            # self.layercapture.capture_udp(pkt["UDP"])
        if(pkt.haslayer(scapy.TCP)):
            self.logger.print_log_info("TCP")
            # self.layercapture.capture_tcp(pkt["TCP"])
        if(pkt.haslayer(scapy.DNS)):
            self.logger.print_log_info("DNS")
            # self.layercapture.capture_dns(pkt["DNS"])
        if(pkt.haslayer(scapy.ICMP)):
            self.logger.print_log_info("ICMP")
            # self.layercapture.capture_icmp(pkt["ICMP"])
        if(pkt.haslayer(scapy.ARP)):
            self.logger.print_log_info("ARP")
            # self.layercapture.capture_arp(pkt["ARP"])

        # print(pkt["UDP"].load)
        # print(pkt["ICMP"].show())

    def sniffing(self):
        # scapy.load_layer("tls")
        # scapy.load_layer("http")
        scapy.sniff(iface=self.interface,store=False,prn=self.process_packet)

    def process_packet(self,pkt):
        # capture = Capture()
        # print(packet.show())
        # print(packet.get_field('dst'))
        
        try:
            # print(packet.show2())
            # print(packet.dst)
            # print(packet.src)
            # print(packet.type)
            # print(packet.nextname)
            # print(packet.payload.layers())
            # print(packet.show())
            # print(packet["UDP"].load)
            # bytes_to_hex(packet["UDP"].load)
            # print(packet["TCP"].show())
            # print(packet["Raw"].show())
            # print(str(packet.payload) + "\n \n")
            # self.http_header(pkt)
            self.analyse_packet(pkt)
            pass
        except Exception as e:
            print(e)
            pass

    @staticmethod
    def packet_sniffing():
        layercapture = LayerCapture()
        packetcapture = PacketCapture("wlo1",layercapture)
        packetcapture.sniffing()
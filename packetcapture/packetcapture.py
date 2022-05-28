import os
import sys
import scapy.all as scapy
from scapy.layers.http import *

# Append parent directory to import path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from logger.logger import Logger

class PacketCapture:
    def __init__(self,interface,layercapture):
        self.interface = interface
        self.logger = Logger("PACKETCAPTURE")

    def analyse_packet(self,pkt):
        if(pkt.haslayer(scapy.UDP)):
            self.logger.print_log_info("UDP")
        if(pkt.haslayer(scapy.TCP)):
            self.logger.print_log_info("TCP")
        if(pkt.haslayer(scapy.DNS)):
            self.logger.print_log_info("DNS")
        if(pkt.haslayer(scapy.ICMP)):
            self.logger.print_log_info("ICMP")
        if(pkt.haslayer(scapy.ARP)):
            self.logger.print_log_info("ARP")

    def sniffing(self):
        # scapy.load_layer("tls")
        # scapy.load_layer("http")
        scapy.sniff(iface=self.interface,store=False,prn=self.process_packet)

    def process_packet(self,pkt):
        try:
            self.analyse_packet(pkt)
        except Exception as e:
            print(e)
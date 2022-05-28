import os
import sys
from collections import deque
from layercapture import LayerCapture
import scapy.all as scapy
from scapy.layers.http import *

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.dbhelper import DBHelper
from logger.logger import Logger
from packetcapture.packetcapture import PacketCapture

queries = {"all":0, "contents":1, "protocol":2, "src_dest":3}

class Detection():
    def __init__(self):
        self.layercapture = LayerCapture()
        self.logger = Logger("DETECTION")
        self.setRulesFromDB(1)

    def getRulesFromDB(self,q):
        dbHelper = DBHelper()

        if(q == 0):
            records = dbHelper.select_rules()
        elif(q == 1):
            records = dbHelper.select_rules_only_contents()
        elif(q == 2):
            records = dbHelper.select_rules_only_protocol()
        elif(q == 3):
            records = dbHelper.select_rules_only_src_dest()

        # i=0
        # for row in records:
        #     print(row[0])
        #     if(i == 5):
        #         break
        #     i=i+1
        return records

    def setRulesFromDB(self,q):
        self.contents = self.getRulesFromDB(1)

    def compareContents(self):
        self.logger.print_log_info("Queue Processing...")
        data = self.layercapture.removeContentFromQueue()
        for i in range(len(self.contents)):
            if str(self.contents[i]) != "('',)":
                if data in self.contents[i]:
                    print("!Found! - " + str(self.contents[i]))
                    break

    def analyse_packet(self,pkt):
        if(pkt.haslayer(scapy.UDP)):
            self.logger.print_log_info("UDP")
            self.layercapture.capture_udp(pkt["UDP"])
        if(pkt.haslayer(scapy.TCP)):
            self.logger.print_log_info("TCP")
            self.layercapture.capture_udp(pkt["TCP"])
        if(pkt.haslayer(scapy.DNS)):
            self.logger.print_log_info("DNS")
        if(pkt.haslayer(scapy.ICMP)):
            self.logger.print_log_info("ICMP")
        if(pkt.haslayer(scapy.ARP)):
            self.logger.print_log_info("ARP")
        if(self.layercapture.contentsQueue):
            self.compareContents()

    def sniffing(self,interface):
        # scapy.load_layer("tls")
        # scapy.load_layer("http")
        scapy.sniff(iface=interface,store=False,prn=self.process_packet)

    def process_packet(self,pkt):
        try:
            self.analyse_packet(pkt)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    detection = Detection()
    detection.sniffing("wlo1")
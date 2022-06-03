import os
import sys

from layercapture import LayerCapture
import scapy.all as scapy
from scapy.layers.http import *
from detection_rules import DetectionRules
from detection_alert import DetectionAlert

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.dbhelper import DBHelper
from logger.logger import Logger
from packetcapture.packetcapture import PacketCapture
from models.alert import Alert

queries = {"all":0, "contents":1, "protocol":2, "src_dest":3}

class Detection():
    def __init__(self):
        self.layercapture = LayerCapture()
        self.logger = Logger("DETECTION")
        self.setRulesFromDB()
        self.detectionRules = DetectionRules(self.src_dst)
        self.detectionAlert = DetectionAlert()

    def getRulesFromDB(self,q):
        dbHelper = DBHelper()

        if(q == 0):
            records = dbHelper.select_rules()
        elif(q == 1):
            records = dbHelper.select_rules_only_contents()
        elif(q == 2):
            records = dbHelper.select_rules_only_protocol()
        elif(q == 3):
            records = dbHelper.select_rules_only_src_dst()

        # i=0
        # for row in records:
        #     print(row[0])
        #     if(i == 5):
        #         break
        #     i=i+1
        return records

    def setRulesFromDB(self):
        self.all_rules = self.getRulesFromDB(0)
        self.contents = self.getRulesFromDB(1)
        self.protocol = self.getRulesFromDB(2)
        self.src_dst = self.getRulesFromDB(3)

    def isBlank(self,myString):
        return not (myString and myString.strip())

    def isNotBlank(self,myString):
        return bool(myString and myString.strip())

    def selectProtocol(self,protocol):
        match protocol:
            case 1:
                return "icmp"
            case 6:
                return "tcp"
            case 17:
                return "udp"

    def compareContents(self):
        self.logger.print_log_info("Queue Processing...")
        q = self.layercapture.removeContentFromQueue()
        data = q['data']
        ip_src = q['ip_src']
        ip_dst = q['ip_dst']
        port_src = q['port_src']
        port_dst = q['port_dst']
        protocol = q['protocol']
        tcp_data = q['tcp_data']
        udp_data = q['udp_data']
        _protocol = self.selectProtocol(protocol)

        for i in range(len(self.contents)):
            _contentsList = str(self.contents[i][0]).split(" ")
            if(self.protocol[i][0] != _protocol):
                continue
            
            res = self.detectionRules.checkAll(i,self.contents[i],data,_contentsList,protocol,tcp_data,udp_data,ip_src,ip_dst,port_src,port_dst)
            if(res == 0):
                self.detectionAlert.createAlert(self.all_rules[i],ip_src,ip_dst,port_src,port_dst)


    def analyse_packet(self,pkt):
        if(pkt.haslayer(scapy.Ether)):
            self.logger.print_log_info("Ether")
            self.layercapture.capture_ether(pkt["Ether"])
        # if(pkt.haslayer(scapy.UDP)):
        #     self.logger.print_log_info("UDP")
        #     self.layercapture.capture_udp(pkt["UDP"])
        # if(pkt.haslayer(scapy.TCP)):
        #     self.logger.print_log_info("TCP")
        #     self.layercapture.capture_tcp(pkt["TCP"])
        # if(pkt.haslayer(scapy.DNS)):
        #     self.logger.print_log_info("DNS")
        # if(pkt.haslayer(scapy.ICMP)):
        #     self.logger.print_log_info("ICMP")
        # if(pkt.haslayer(scapy.ARP)):
        #     self.logger.print_log_info("ARP")
        # if(self.layercapture.contentsQueue):
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
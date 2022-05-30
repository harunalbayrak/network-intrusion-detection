import os
import sys
import re
import time
from datetime import datetime
from collections import deque
from layercapture import LayerCapture
import scapy.all as scapy
from scapy.layers.http import *

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
   
        _protocol = ""

        if(protocol == 1):
            _protocol = "icmp"
        elif(protocol == 6):
            _protocol = "tcp"
        elif(protocol == 17):
            _protocol = "udp"

        # print(ip_src)

        for i in range(len(self.contents)):
            nocontent = 0
            if(len(self.contents[i][0]) == 0):
                nocontent = 1

            _contentsList = str(self.contents[i][0]).split(" ")
            if(self.protocol[i][0] != _protocol):
                continue
            
            if(self.src_dst[i][0] == "$HOME_NET"): # src ip
                ip_src_list = ip_src.split('.')
                # print(ip_src_list)
                if(ip_src_list[0] != 10 and ip_src_list[0] != 172 and ip_src_list[0] != 192):
                    continue
                if(ip_src_list[0] == 172 and not (ip_src_list[1] >= 16 and ip_src_list[1] <= 31)):
                    continue
                if(ip_src_list[0] == 192 and not (ip_src_list[1] == 168)):
                    continue
            
            if(self.src_dst[i][0] == "$EXTERNAL_NET"): # src ip
                ip_src_list = ip_src.split('.')
                if(ip_src_list[0] == 10 or ip_src_list[0] == 172 or ip_src_list[0] == 192):
                    continue
                if(ip_src_list[0] == 172 and (ip_src_list[1] >= 16 and ip_src_list[1] <= 31)):
                    continue
                if(ip_src_list[0] == 192 and (ip_src_list[1] == 168)):
                    continue

            if(self.src_dst[i][0][0] == '['): # src ip
                _src_dst = self.src_dst[i][0].replace('[','').replace(']','') 
                ip_src_list = _src_dst.split(',')
                for ip_src_x in ip_src_list:
                    if(ip_src_x == ip_src):
                        now = datetime.now()
                        current_time = now.strftime("%H:%M:%S")
                        alert = Alert(current_time,"High",self.all_rules[i][0],self.all_rules[i][2],self.all_rules[i][3],ip_src,port_src,ip_dst,port_dst,self.all_rules[i][8],self.all_rules[i][9],self.all_rules[i][10],self.all_rules[i][11])
                        # print(f"Found: {ip_src}")
                        print(alert)
                        break


            if(self.src_dst[i][2] == "$HOME_NET"): # dst ip
                ip_dst_list = ip_dst.split('.')
                # print(ip_src_list)
                if(ip_dst_list[0] != 10 and ip_dst_list[0] != 172 and ip_dst_list[0] != 192):
                    continue
                if(ip_dst_list[0] == 172 and not (ip_dst_list[1] >= 16 and ip_dst_list[1] <= 31)):
                    continue
                if(ip_dst_list[0] == 192 and not (ip_dst_list[1] == 168)):
                    continue
            
            if(self.src_dst[i][2] == "$EXTERNAL_NET"): # dst ip
                ip_dst_list = ip_dst.split('.')
                if(ip_dst_list[0] == 10 or ip_dst_list[0] == 172 or ip_dst_list[0] == 192):
                    continue
                if(ip_dst_list[0] == 172 and (ip_dst_list[1] >= 16 and ip_dst_list[1] <= 31)):
                    continue
                if(ip_dst_list[0] == 192 and (ip_dst_list[1] == 168)):
                    continue
            
            if(self.src_dst[i][1] == "$HTTP_PORTS"): # src port
                if(port_src != 80 and port_src != 443):
                    continue

            if(self.src_dst[i][1].isnumeric()): # src port
                if(int(self.src_dst[i][1]) != port_src):
                    continue

            if(self.src_dst[i][3] == "$HTTP_PORTS"): # dst port
                if(port_dst != 80 and port_dst != 443):
                    continue

            if(self.src_dst[i][3].isnumeric()): # dst port
                if(int(self.src_dst[i][3]) != port_dst):
                    continue

            # self.logger.print_log_info(len(_contentsList))
            flag = 0
            if(nocontent == 0):
                for j in _contentsList:
                    if(j == ''):
                        continue
                    # self.logger.print_log_info(j)

                    pattern = "[0-9a-f]+"
                    result = re.fullmatch(pattern, j)
                    if result:
                        isHexadecimal = 1
                    else:
                        isHexadecimal = 0	

                    if(isHexadecimal == 0):
                        # self.logger.print_log_info(j)
                        if j in data:
                            flag = flag + 1
                            continue

                    if(isHexadecimal == 1):
                        # self.logger.print_log_info(j)
                        if protocol == 6 and j in tcp_data:
                            flag = flag + 1
                            continue
                        if protocol == 17 and j in udp_data:
                            flag = flag + 1
                            continue
                
                if(flag == len(_contentsList)):
                    if(flag == 1 and len(j) > 3):
                        print(data + " - !Found! - " + str(i) + " - " + j)
                    elif(flag != 1):
                        print(data + " - !Found! - " + str(i) + " - " + j)
            else:
                pass


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
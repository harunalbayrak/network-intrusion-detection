import os
import sys
import re

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from logger.logger import Logger

class DetectionRules:
    def __init__(self,src_dst):
        self.src_dst = src_dst
        self.logger = Logger("DETECTION")

    def checkSourceIP(self,i,ip_src):
        if(self.src_dst[i][0] == "$HOME_NET"): # src ip
            ip_src_list = ip_src.split('.')
            # print(ip_src_list)
            if(ip_src_list[0] != 10 and ip_src_list[0] != 172 and ip_src_list[0] != 192):
                return -1
            if(ip_src_list[0] == 172 and not (ip_src_list[1] >= 16 and ip_src_list[1] <= 31)):
                return -1
            if(ip_src_list[0] == 192 and not (ip_src_list[1] == 168)):
                return -1
            
        if(self.src_dst[i][0] == "$EXTERNAL_NET"): # src ip
            ip_src_list = ip_src.split('.')
            if(ip_src_list[0] == 10 or ip_src_list[0] == 172 or ip_src_list[0] == 192):
                return -1
            if(ip_src_list[0] == 172 and (ip_src_list[1] >= 16 and ip_src_list[1] <= 31)):
                return -1
            if(ip_src_list[0] == 192 and (ip_src_list[1] == 168)):
                return -1

        if(self.src_dst[i][0][0] == '['): # src ip
            _src_dst = self.src_dst[i][0].replace('[','').replace(']','') 
            ip_src_list = _src_dst.split(',')
            for ip_src_x in ip_src_list:
                if(ip_src_x == ip_src):
                    return 0
                    # now = datetime.now()
                    # current_time = now.strftime("%H:%M:%S")
                    # alert = Alert(current_time,"High",self.all_rules[i][0],self.all_rules[i][2],self.all_rules[i][3],ip_src,port_src,ip_dst,port_dst,self.all_rules[i][8],self.all_rules[i][9],self.all_rules[i][10],self.all_rules[i][11])
                    # print(f"Found: {ip_src}")
                    # print(alert)
    
    def checkDestinationIP(self,i,ip_dst):
        if(self.src_dst[i][2] == "$HOME_NET"): # dst ip
            ip_dst_list = ip_dst.split('.')
            # print(ip_src_list)
            if(ip_dst_list[0] != 10 and ip_dst_list[0] != 172 and ip_dst_list[0] != 192):
                return -1
            if(ip_dst_list[0] == 172 and not (ip_dst_list[1] >= 16 and ip_dst_list[1] <= 31)):
                return -1
            if(ip_dst_list[0] == 192 and not (ip_dst_list[1] == 168)):
                return -1
        
        if(self.src_dst[i][2] == "$EXTERNAL_NET"): # dst ip
            ip_dst_list = ip_dst.split('.')
            if(ip_dst_list[0] == 10 or ip_dst_list[0] == 172 or ip_dst_list[0] == 192):
                return -1
            if(ip_dst_list[0] == 172 and (ip_dst_list[1] >= 16 and ip_dst_list[1] <= 31)):
                return -1
            if(ip_dst_list[0] == 192 and (ip_dst_list[1] == 168)):
                return -1

    def checkSourcePort(self,i,port_src):
        if(self.src_dst[i][1] == "$HTTP_PORTS"): # src port
            if(port_src != 80 and port_src != 443):
                return -1

        if(self.src_dst[i][1].isnumeric()): # src port
            if(int(self.src_dst[i][1]) != port_src):
                return -1
    
    def checkDestinationPort(self,i,port_dst):
        if(self.src_dst[i][3] == "$HTTP_PORTS"): # dst port
            if(port_dst != 80 and port_dst != 443):
                return -1

        if(self.src_dst[i][3].isnumeric()): # dst port
            if(int(self.src_dst[i][3]) != port_dst):
                return -1

    def checkIPandPort(self,i,ip_src,ip_dst,port_src,port_dst):
        res = self.checkSourceIP(i,ip_src)
        if(res == -1):
            return -1

        res = self.checkDestinationIP(i,ip_dst)
        if(res == -1):
            return -1
       
        res = self.checkSourcePort(i,port_src)
        if(res == -1):
            return -1

        res = self.checkDestinationPort(i,port_src)
        if(res == -1):
            return -1

        return 0

    def checkContent(self,i,data,_contentsList,protocol,tcp_data,udp_data):
        flag = 0

        # print(_contentsList)
        for j in _contentsList:
            if(j == ''):
                flag = flag + 1
                continue

            pattern = "[0-9a-f]+"
            result = re.fullmatch(pattern, j)
            if result:
                isHexadecimal = 1
            else:
                isHexadecimal = 0	

            if(isHexadecimal == 0):
                if j in data:
                    flag = flag + 1
                    continue

            if(isHexadecimal == 1):
                if protocol == 6 and j in tcp_data:
                    flag = flag + 1
                    continue
                if protocol == 17 and j in udp_data:
                    flag = flag + 1
                    continue
        
        # if(flag != 0):
            # print(f"Flag: {flag} - {len(_contentsList)}, {_contentsList}")
        if(flag == len(_contentsList)):
            if(flag > 2):
                # print(f"Flag: {flag} - {len(_contentsList)}, {_contentsList}")
                return 0
            elif(flag != 1):
                return 0

    def checkAll(self,i,content,data,_contentsList,protocol,tcp_data,udp_data,ip_src,ip_dst,port_src,port_dst):
        flag = 0
        res = self.checkIPandPort(i,ip_src,ip_dst,port_src,port_dst)
        if(res == -1):
            return -1
        # elif(res == 0):
            self.logger(f"Satisfied IP and PORT of the Packet")
            # return 0

        if(len(content[0]) == 0):
            return -1

        res = self.checkContent(i,data,_contentsList,protocol,tcp_data,udp_data)
        if(res == -1):
            return -1
        elif(res == 0):
            print(_contentsList)
            return 0
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.statistics import IPStatistics, PortStatistics, ProtocolStatistics
from database.dbhelper import DBHelper

class DetectionStatistics:
    def __init__(self):
        self.dbHelper = DBHelper()
        self.ip_src_buffer = []
        self.ip_dst_buffer = []
        self.port_src_buffer = []
        self.port_dst_buffer = []
        self.protocol_buffer = []
        self.time_limit = 60.0
        pass

    def returnBuffer(self,num):
        if(num == 0):
            return self.ip_src_buffer
        elif(num == 1):
            return self.ip_dst_buffer
        elif(num == 2):
            return self.port_src_buffer
        elif(num == 3):
            return self.port_dst_buffer
        elif(num == 4):
            return self.protocol_buffer

    def checkStatistics(self,stat_text,stat,num):
        new_time = time.time()
        for i in range(0,len(self.returnBuffer(num))):
            stat_i = self.returnBuffer(num)[i][stat_text]
            old_time = self.returnBuffer(num)[i]["time"]
            if(stat == stat_i):
                calculated_time = new_time - old_time
                if(calculated_time > self.time_limit):
                    self.returnBuffer(num).remove(self.returnBuffer(num)[i])
                    return self.returnBuffer(num)[i]["count"]
                else:
                    return -1
        return 0

    def addStatistics(self,ip_src,ip_dst,port_src,port_dst,protocol):
        res = self.checkStatistics("ip_src",ip_src,0)
        if(res >= 0):
            count = res + 1
            _stat = {"ip_src":ip_src, "count":count, "time":time.time()}
            stat = IPStatistics(ip_src,"country","src",count)
            self.dbHelper.update_statistics(2,(count,ip_src,"src"))
            self.dbHelper.insert_statistics(2,stat)
            self.ip_src_buffer.append(_stat)

        res = self.checkStatistics("ip_dst",ip_dst,1)
        if(res >= 0):
            count = res + 1
            _stat = {"ip_dst":ip_dst, "count":count, "time":time.time()}
            stat = IPStatistics(ip_dst,"country","dst",count)
            self.dbHelper.update_statistics(2,(count,ip_src,"dst"))
            self.dbHelper.insert_statistics(2,stat)
            self.ip_dst_buffer.append(_stat)

        res = self.checkStatistics("port_src",port_src,2)
        if(res >= 0):
            count = res + 1
            _stat = {"port_src":port_src, "count":count, "time":time.time()}
            stat = PortStatistics(str(port_src),"src",count)
            self.dbHelper.update_statistics(3,(count,str(port_src),"src"))
            self.dbHelper.insert_statistics(3,stat)
            self.port_src_buffer.append(_stat)

        res = self.checkStatistics("port_dst",port_dst,3)
        if(res >= 0):
            count = res + 1
            _stat = {"port_dst":port_dst, "count":count, "time":time.time()}
            stat = PortStatistics(str(port_dst),"dst",count)
            self.dbHelper.update_statistics(3,(count,str(port_dst),"dst"))
            self.dbHelper.insert_statistics(3,stat)
            self.port_dst_buffer.append(_stat)

        res = self.checkStatistics("protocol",protocol,4)
        if(res >= 0):
            count = res + 1
            _stat = {"protocol":protocol, "count":count, "time":time.time()}
            stat = ProtocolStatistics(str(protocol),count)
            self.dbHelper.update_statistics(4,(count,str(protocol)))
            self.dbHelper.insert_statistics(4,stat)
            self.protocol_buffer.append(_stat)
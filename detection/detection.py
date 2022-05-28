import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.dbhelper import DBHelper
from packetcapture.packetcapture import PacketCapture
from logger.logger import Logger

queries = {"all":0, "contents":1, "protocol":2, "src_dest":3}

class Detection():
    def __init__(self):
        self.logger = Logger("DETECTION")

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

        i=0
        for row in records:
            print(row[0])
            if(i == 5):
                break
            i=i+1
        return records

    def packetSniffing(self):
        PacketCapture.packet_sniffing()

if __name__ == "__main__":
    detection = Detection()
    detection.getRulesFromDB(3)
    detection.packetSniffing()
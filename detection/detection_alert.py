import os
import sys
import time
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.alert import Alert
from database.dbhelper import DBHelper

class DetectionAlert:
    def __init__(self):
        self.dbHelper = DBHelper()
        self.alerts = []
        self.time_limit = 120.0
        pass

    def checkIsAddable(self,alert2):
        for i in range(0,len(self.alerts)):
            alert = self.alerts[i]["alert"]
            alert_time = self.alerts[i]["time"]
            if(alert.sid == alert2["alert"].sid):
                old_time = alert_time
                new_time = alert2["time"]
                if(new_time - old_time > self.time_limit):
                    self.alerts.remove(self.alerts[i])
                    return True
                else:
                    return False
        return True

    def createAlert(self,rule,ip_src,ip_dst,port_src,port_dst):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        alert = Alert(current_time,"High",rule[2],rule[3],ip_src,port_src,ip_dst,port_dst,rule[8],rule[9],rule[10],rule[11])
        _alert = {"alert":alert, "time": time.time()}

        if(self.checkIsAddable(_alert)):
            self.alerts.append(_alert)
            self.insert_alert_db(alert)
            print(alert)
            
    def insert_alert_db(self,alert):
        self.dbHelper.insert_alert(alert)
import os
import sys
import time
from datetime import datetime, date

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.alert import Alert
from database.dbhelper import DBHelper

class DetectionAlert:
    def __init__(self):
        self.dbHelper = DBHelper()
        self.alerts = []
        self.time_limit = 120.0
        self.priority_time_limit = 180.0
        pass
    
    def checkIsAddable(self,alert2):
        for i in range(0,len(self.alerts)):
            alert = self.alerts[i]["alert"]
            alert_time = self.alerts[i]["time"]
            if(alert.sid == alert2["alert"].sid):
                old_time = alert_time
                new_time = alert2["time"]
                calculated_time = new_time - old_time
                if(calculated_time > self.time_limit):
                    self.alerts.remove(self.alerts[i])
                    if(alert.priority == "Low" and calculated_time < self.priority_time_limit):
                        return 1
                    elif(alert.priority == "Medium" and calculated_time < self.priority_time_limit):
                        return 2
                    elif(alert.priority == "High" and calculated_time < self.priority_time_limit):
                        return 3
                    else:
                        return 0
                else:
                    return -1
        return 0

    def createAlert(self,rule,ip_src,ip_dst,port_src,port_dst):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_day = date.today()
        alert = Alert(current_time,current_day,"Low",rule[2],rule[3],ip_src,port_src,ip_dst,port_dst,rule[8],rule[9],rule[10],rule[11])
        _alert = {"alert":alert, "time": time.time()}
        
        isAddable = self.checkIsAddable(_alert)
        if(isAddable >= 0):
            if(isAddable == 0):
                _priority = "Low"
            elif(isAddable == 1):
                _priority = "Medium"
            elif(isAddable >= 2):
                _priority = "High"
            else:
                _priority = "Low"

            alert.priority = _priority
            self.alerts.append(_alert)
            self.insert_alert_db(alert)
            print(alert)
            
    def insert_alert_db(self,alert):
        self.dbHelper.insert_alert(alert)
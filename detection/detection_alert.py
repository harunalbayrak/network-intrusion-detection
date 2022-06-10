import os
import sys
import time
from datetime import datetime, date

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.alert import Alert
from models.statistics import DashboardWeekdayStatistics
from database.dbhelper import DBHelper
from logger.logger import Logger

class DetectionAlert:
    def __init__(self):
        self.dbHelper = DBHelper()
        self.alerts = []
        self.time_limit = 120.0
        self.priority_time_limit = 180.0
        self.logger = Logger("DETECTION")
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

    def createAlert(self,rule,ip_src,ip_dst,port_src,port_dst,i):
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
            self.logger.print_log_warning(f"Alert! Rule Number: {i} - {alert.class_type} - {alert.message} - {alert.protocol} - {alert.source_ip}:{alert.source_port} -> {alert.destination_ip}:{alert.destination_port}")
            
            weekday = datetime.today().weekday()
            record = self.dbHelper.select_weekday(weekday)

            stat = DashboardWeekdayStatistics(weekday,str(record[0]+1))
            self.dbHelper.update_statistics(6,stat.to_tuple2())

            # try:
                # self.dbHelper.insert_statistics(6,stat)
            # except:
                # self.dbHelper.update_statistics(6,stat.to_tuple2())
            
    def insert_alert_db(self,alert):
        self.dbHelper.insert_alert(alert)
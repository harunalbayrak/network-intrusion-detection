import os
import sys
import math
from datetime import date, datetime
from fastapi import Depends, FastAPI, Body, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import dbhelper

# Append parent directory to import path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.rule import Rule
from models.alert import Alert
from models.statistics import IPStatistics, PortStatistics, ProtocolStatistics, DashboardWeekdayStatistics
from logger.logger import Logger

# Initiliaze
dbhelper.Base.metadata.create_all(bind=dbhelper.engine)
app = FastAPI()
logger = Logger("GUI")

# Static file serv
app.mount("/static", StaticFiles(directory="src"), name="static")

# Jinja2 template directory
templates = Jinja2Templates(directory="src")

daily_alert_counts = [90, 39, 40, 52, 20, 15, 28]
total_alerts = [20, 59, 89, 141, 161, 176, 204]
total_rules = [20000, 20002, 19996, 20007, 20014, 20022, 20022, 20030, 20035, 20020, 20020, 20022]
priority_levels = [0,0,0]
dashboard_card_icons = ["error","error","graphic_eq","person"]
dashboard_card_names = ["Today's Alerts","Total Alerts","Total Rules","Total Users"]
dashboard_card_values = [3,392,20000,2]

top_source_ips_key = ["","","","","","","",""]
top_source_ips_value = [0,0,0,0,0,0,0,0]

top_destination_ips_key = ["","","","","","","",""]
top_destination_ips_value = [0,0,0,0,0,0,0,0]

top_source_ports_key = ["","","","","","","",""]
top_source_ports_value = [0,0,0,0,0,0,0,0]

top_destination_ports_key = ["","","","","","","",""]
top_destination_ports_value = [0,0,0,0,0,0,0,0]

top_protocols_key = ["","","","","","","",""]
top_protocols_value = [0,0,0,0,0,0,0,0]

# rules = [Rule("alert",2009248,"tcp","ET SHELLCODE Lindau (linkbot) xor Decoder Shellcode"),Rule("alert",26075,"tcp","MALWARE-CNC Win.Trojan.Zbot variant in.php outbound connection"),Rule("alert",26965,"tcp","MALWARE-CNC Win.Trojan.Win32 Facebook Secure Cryptor C2"),Rule("alert",57067,"udp","SERVER-OTHER OpenBSD ISAKMP denial of service attempt")]
# alerts = [Alert("21.05.2018 / 17:56:31","High","Server-MySQL","client overflow attempt"),Alert("21.05.2018 / 17:50:22","High","Server-MySQL","Bittorrent uTP peer request"),Alert("21.05.2018 / 16:42:11","Low","Server-MySQL","OpenSSL TLS change cipher spec protocol denial of service"),Alert("21.05.2018 / 14:54:02","High","Server-MySQL","ssh CRC32 overflow filter"),Alert("21.05.2018 / 10:05:53","Medium","Server-MySQL","Sipvicious User-Agent detected"),Alert("21.05.2018 / 08:44:09","High","Server-MySQL","Win.Trojan.Rombrast Trojan outbound connection")]

def get_db():
    db = dbhelper.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/",response_class=RedirectResponse)
def index(request: Request):
    return RedirectResponse(url="/dashboard")

@app.get("/dashboard",response_class=HTMLResponse)
def index(request: Request, db:dbhelper.Session = Depends(get_db)):
    current_day = str(date.today())
    weekday = datetime.today().weekday()

    total = 0
    for i in range(0,7):
        try:
            daily_alert_counts[i] = db.query(DashboardWeekdayStatistics).filter(DashboardWeekdayStatistics.weekday == i).one().count
            total = total + daily_alert_counts[i]
            total_alerts[i] = total
        except:
            daily_alert_counts[i] = 0
            total_alerts[i] = total

    rules = db.query(Rule).all()
    alerts = db.query(Alert).all()
    today_alerts = db.query(Alert).filter(Alert.day == current_day).all()
    dashboard_card_values[2] = len(rules)
    dashboard_card_values[1] = len(alerts)
    dashboard_card_values[0] = len(today_alerts)

    for i in range(0,12):
        total_rules[i] = len(rules)

    low_priorities = db.query(Alert).filter(Alert.priority == "Low").all()
    medium_priorities = db.query(Alert).filter(Alert.priority == "Medium").all()
    high_priorities = db.query(Alert).filter(Alert.priority == "High").all()
    priority_levels[0] = len(low_priorities)
    priority_levels[1] = len(medium_priorities)
    priority_levels[2] = len(high_priorities)

    return templates.TemplateResponse("pages/dashboard.html",{"request": request,"name":"Dashboard", "dashboard_card_names": dashboard_card_names, "dashboard_card_values":dashboard_card_values, "dashboard_card_icons": dashboard_card_icons, "priority_levels":priority_levels, "daily_alert_counts": daily_alert_counts, "total_alerts": total_alerts, "total_rules": total_rules, "alerts": alerts, "rules": rules})

@app.get("/rules", response_class=HTMLResponse)
def index(request: Request, db:dbhelper.Session = Depends(get_db), page: int = 1):
    start = (page - 1) * 10
    end = start + 10
    rules = db.query(Rule).all()
    last = math.ceil(len(rules) / 10)
    rules = rules[start:end]
    return templates.TemplateResponse("pages/rules.html",{"request": request,"name":"Rules", "rules": rules, "last": last, "page": page})

@app.get("/alerts",response_class=HTMLResponse)
def index(request: Request, db:dbhelper.Session = Depends(get_db), page: int = 1):
    alerts = db.query(Alert).all()
    start = len(alerts) - ((page - 1) * 10)
    end = start - 10
    if(end < 0):
        end = 0
    last = math.ceil(len(alerts) / 10)
    alerts = alerts[end:start]
    return templates.TemplateResponse("pages/alerts.html",{"request": request,"name":"Alerts", "alerts": alerts, "last": last, "page": page})

@app.get("/network",response_class=HTMLResponse)
def index(request: Request, db:dbhelper.Session = Depends(get_db)):
    ipStats = db.query(IPStatistics).filter(IPStatistics.type == "src").order_by(IPStatistics.count.desc()).all()
    for i in range(0,len(ipStats)):
        if(i == 8):
            break
        top_source_ips_key[i] = ipStats[i].ip
        top_source_ips_value[i] = ipStats[i].count

    ipStats = db.query(IPStatistics).filter(IPStatistics.type == "dst").order_by(IPStatistics.count.desc()).all()
    for i in range(0,len(ipStats)):
        if(i == 8):
            break
        top_destination_ips_key[i] = ipStats[i].ip
        top_destination_ips_value[i] = ipStats[i].count

    portStats = db.query(PortStatistics).filter(PortStatistics.type == "src").order_by(PortStatistics.count.desc()).all()
    for i in range(0,len(portStats)):
        if(i == 8):
            break
        top_source_ports_key[i] = portStats[i].port
        top_source_ports_value[i] = portStats[i].count

    portStats = db.query(PortStatistics).filter(PortStatistics.type == "dst").order_by(PortStatistics.count.desc()).all()
    for i in range(0,len(portStats)):
        if(i == 8):
            break
        top_destination_ports_key[i] = portStats[i].port
        top_destination_ports_value[i] = portStats[i].count

    protocolStats = db.query(ProtocolStatistics).order_by(ProtocolStatistics.count.desc()).all()
    for i in range(0,len(protocolStats)):
        if(i == 8):
            break
        top_protocols_key[i] = protocolStats[i].protocol
        top_protocols_value[i] = protocolStats[i].count

    return templates.TemplateResponse("pages/network.html",{"request": request,"name":"Network","c1_key":top_source_ips_key,"c1_value":top_source_ips_value,"c2_key":top_destination_ips_key,"c2_value":top_destination_ips_value,"c3_key":top_source_ports_key,"c3_value":top_source_ports_value,"c4_key":top_destination_ports_key,"c4_value":top_destination_ports_value,"c5_key":top_protocols_key,"c5_value":top_protocols_value})
    # return templates.TemplateResponse("pages/network.html",{"request": request,"name":"Network", "alerts": alerts})
import os
import sys
import math
from datetime import date
from fastapi import Depends, FastAPI, Body, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import dbhelper

# Append parent directory to import path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.rule import Rule
from models.alert import Alert
from logger.logger import Logger

# Initiliaze
dbhelper.Base.metadata.create_all(bind=dbhelper.engine)
app = FastAPI()
logger = Logger("GUI")

# Static file serv
app.mount("/static", StaticFiles(directory="src"), name="static")

# Jinja2 template directory
templates = Jinja2Templates(directory="src")

dashboard_card_icons = ["error","error","graphic_eq","person"]
dashboard_card_names = ["Today's Alerts","Total Alerts","Total Rules","Total Users"]
dashboard_card_values = [3,392,20000,2]

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
    rules = db.query(Rule).all()
    alerts = db.query(Alert).all()
    current_day = str(date.today())
    today_alerts = db.query(Alert).filter(Alert.day == current_day).all()
    dashboard_card_values[2] = len(rules)
    dashboard_card_values[1] = len(alerts)
    dashboard_card_values[0] = len(today_alerts)
    return templates.TemplateResponse("pages/dashboard.html",{"request": request,"name":"Dashboard", "dashboard_card_names": dashboard_card_names, "dashboard_card_values":dashboard_card_values, "dashboard_card_icons": dashboard_card_icons, "alerts": alerts, "rules": rules})

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
def index(request: Request):
    return templates.TemplateResponse("pages/network.html",{"request": request,"name":"Network"})
    # return templates.TemplateResponse("pages/network.html",{"request": request,"name":"Network", "alerts": alerts})
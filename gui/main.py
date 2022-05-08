from fastapi import FastAPI, Body, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from models.rule import Rule
from models.alert import Alert

# Initiliaze
app = FastAPI()

# Static file serv
app.mount("/static", StaticFiles(directory="src"), name="static")

# Jinja2 template directory
templates = Jinja2Templates(directory="src")

dashboard_card_icons = ["error","error","graphic_eq","person"]
dashboard_card_names = ["Today's Alerts","Total Alerts","Total Rules","Total Users"]
dashboard_card_values = [3,392,20000,2]

rules = [Rule("alert",2009248,"tcp","ET SHELLCODE Lindau (linkbot) xor Decoder Shellcode"),Rule("alert",2009248,"tcp","ET SHELLCODE Lindau (linkbot) xor Decoder Shellcode"),Rule("alert",2009248,"tcp","ET SHELLCODE Lindau (linkbot) xor Decoder Shellcode"),Rule("alert",2009248,"tcp","ET SHELLCODE Lindau (linkbot) xor Decoder Shellcode")]
alerts = [Alert("21.05.2018 / 17:56:31","High","Server-MySQL","client overflow attempt"),Alert("21.05.2018 / 17:50:22","High","Server-MySQL","Bittorrent uTP peer request"),Alert("21.05.2018 / 16:42:11","Low","Server-MySQL","OpenSSL TLS change cipher spec protocol denial of service"),Alert("21.05.2018 / 14:54:02","High","Server-MySQL","ssh CRC32 overflow filter"),Alert("21.05.2018 / 10:05:53","Medium","Server-MySQL","Sipvicious User-Agent detected"),Alert("21.05.2018 / 08:44:09","High","Server-MySQL","Win.Trojan.Rombrast Trojan outbound connection")]

@app.get("/",response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("pages/dashboard.html",{"request": request, "name":"Dashboard"})

@app.get("/dashboard",response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("pages/dashboard.html",{"request": request,"name":"Dashboard", "dashboard_card_names": dashboard_card_names, "dashboard_card_values":dashboard_card_values, "dashboard_card_icons": dashboard_card_icons, "alerts": alerts})

@app.get("/rules",response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("pages/rules.html",{"request": request,"name":"Rules", "rules": rules})

@app.get("/alerts",response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("pages/alerts.html",{"request": request,"name":"Alerts", "alerts": alerts})

@app.get("/network",response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("pages/network.html",{"request": request,"name":"Network", "alerts": alerts})
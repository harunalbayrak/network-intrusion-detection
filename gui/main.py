from fastapi import FastAPI, Body, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from rule import Rule

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

@app.get("/",response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("pages/dashboard.html",{"request": request, "name":"Dashboard"})

@app.get("/dashboard",response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("pages/dashboard.html",{"request": request,"name":"Dashboard", "dashboard_card_names": dashboard_card_names, "dashboard_card_values":dashboard_card_values, "dashboard_card_icons": dashboard_card_icons})

@app.get("/rules",response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("pages/rules.html",{"request": request,"name":"Rules", "rules": rules})
from fastapi import FastAPI, Body, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Initiliaze
app = FastAPI()

# Static file serv
app.mount("/static", StaticFiles(directory="src"), name="static")

# Jinja2 template directory
templates = Jinja2Templates(directory="src")

@app.get("/",response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html",{"request": request, "name":"Dashboard"})

@app.get("/dashboard",response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("pages/dashboard.html",{"request": request,"name":"Dashboard"})

@app.get("/rules",response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("pages/rules.html",{"request": request,"name":"Rules"})
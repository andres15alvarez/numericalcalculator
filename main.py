from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(request, "index.html", { "greeting": "Hello World" })

@app.get("/raices", response_class=HTMLResponse)
def raices(request: Request):
    return templates.TemplateResponse(request, "raices.html", { "greeting": "Hello World" })

@app.get("/sistemas", response_class=HTMLResponse)
def sistemas(request: Request):
    return templates.TemplateResponse(request, "sistemas.html", { "greeting": "Hello World" })

@app.get("/raices-resolucion", response_class=HTMLResponse)
def sistemas(request: Request):
    return templates.TemplateResponse(request, "raices-resolucion.html", { "greeting": "Hello World" })

@app.get("/sistemas-resolucion", response_class=HTMLResponse)
def sistemas(request: Request):
    return templates.TemplateResponse(request, "sistemas-resolucion.html", { "greeting": "Hello World" })

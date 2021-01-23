import json

from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


import giaiPhuongTrinh
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="GiaiTamGiac")
@app.get("/", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get('/giaitoan')
def giaitoan():
    giaiPhuongTrinh.reset()
    kq = giaiPhuongTrinh.run()
    return kq
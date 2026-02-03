from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import random
import string

app = FastAPI()
templates = Jinja2Templates(directory="templates")
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
@app.get("/generate")
async def generate_password(length: int = 12): # Riceve la lunghezza dallo slider
    colori = ["Rosso", "Verde", "Blu", "Giallo", "Nitro", "Cyber", "Mega"]
    oggetti = ["Luna", "Drago", "Cactus", "Pixel", "Vento", "Codice", "Zenit"]
    
    # Genera una base memorabile
    base = random.choice(colori) + random.choice(oggetti)
    
    # Riempie fino alla lunghezza desiderata con numeri e simboli
    chars = string.digits + "!?@#$"
    extra = ''.join(random.choice(chars) for _ in range(max(0, length - len(base))))
    
    password_ai = (base + extra)[:length] # Taglia o mantiene alla lunghezza esatta
    return {"password": password_ai}



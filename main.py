from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import secrets
import string

app = FastAPI()
templates = Jinja2Templates(directory="templates")
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
@app.get("/generate")
async def generate_password(length: int = 12):
    colori = ["Rosso", "Verde", "Blu", "Giallo", "Nitro", "Cyber", "Mega"]
    oggetti = ["Luna", "Drago", "Cactus", "Pixel", "Vento", "Codice", "Zenit"]

    # Genera una base memorabile usando secrets.choice
    base = secrets.choice(colori) + secrets.choice(oggetti)
    # Riempe fino alla lunghezza desiderata con numeri e simboli
    chars = string.digits + "!?@#$" 
    # Calcoliamo quanto manca per raggiungere la lunghezza target
    lunghezza_mancante = max(0, length - len(base))
    extra = ''.join(secrets.choice(chars) for _ in range(lunghezza_mancante))

    # Unisce e assicura la lunghezza esatta
    password_ai = (base + extra)[:length]
    return {"password": password_ai}
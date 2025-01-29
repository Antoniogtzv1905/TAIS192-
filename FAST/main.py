from fastapi import FastAPI  # Importa correctamente FastAPI

app = FastAPI()  # Instancia correctamente FastAPI

# Endpoint home
@app.get("/")

def home():
    return {"hello": "Bienvenido a FastAPI"}  

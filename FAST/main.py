from fastapi import FastAPI  # Importa correctamente FastAPI
from typing import Optional

app = FastAPI(
    title='Mi primer API S192',
    description='DANTONIO',
    version='1.1'
)

usuarios = [
    {"id": 1, "Nombre": "Antonio Gutierrez", "edad": 20},
    {"id": 2, "Nombre": "Daniel Moncada Peña", "edad": 20},
    {"id": 3, "Nombre": "Marco", "edad": 45},
    {"id": 4, "Nombre": "Isabel", "edad": 72}
]

# Endpoint home
@app.get('/', tags=["Hola mundo"])
def home():
    return {"hello": "Bienvenido a FastAPI"}

# Endpoint promedio
@app.get('/promedio', tags=["promedio"])
def promedio():
    return {"promedio": 6.1}

# Endpoint con parámetro obligatorio
@app.get('/Usuario/{id}', tags=["Parametro Obligatorio"])
def consulta_usuario(id: int):
    for usuario in usuarios:
        if usuario["id"] == id:
            return {"mensaje": "Usuario encontrado", "usuario": usuario}
    return {"mensaje": "Usuario no encontrado"}

# Endpoint con parámetro opcional
@app.get('/Usuario/', tags=["Parametro opcional"])
def consulta_usuario_opcional(id: Optional[int] = None):
    if id is not None:
        for usuario in usuarios:
            if usuario["id"] == id:
                return {"mensaje": "Usuario encontrado", "usuario": usuario}
        return {"mensaje": f"Usuario con ID {id} no encontrado"}
    return {"mensaje": "No se proporcionó un ID"}

#endpoint con varios parametro opcionales
@app.get("/usuarios/", tags=["3 parámetros opcionales"])
async def consulta_usuarios(
    usuario_id: Optional[int] = None,
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = []

    for usuario in usuarios:
        if (
            (usuario_id is None or usuario["id"] == usuario_id) and
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios_encontrados": resultados}
    else:
        return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}
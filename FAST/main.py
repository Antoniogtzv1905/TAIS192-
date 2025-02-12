from fastapi import FastAPI, HTTPException
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

# Endpoint con varios parámetros opcionales
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

# Endpoint para buscar un usuario por nombre
@app.get("/usuario_nombre/", tags=["Buscar por nombre"])
def buscar_usuario_por_nombre(nombre: str):
    resultados = [usuario for usuario in usuarios if nombre.lower() in usuario["Nombre"].lower()]
    return {"usuarios_encontrados": resultados}

# Endpoint para agregar un nuevo usuario
@app.post("/usuario/", tags=["Agregar Usuario"])
async def agregar_usuario(usuario: dict):
    # Verifica si ya existe un usuario con el mismo ID
    for existing_user in usuarios:
        if existing_user["id"] == usuario["id"]:
            raise HTTPException(status_code=400, detail="Usuario con este ID ya existe")
    
    # Agregar el nuevo usuario
    usuarios.append(usuario)
    return {"mensaje": "Usuario agregado con éxito", "usuario": usuario}

# Endpoint para actualizar un usuario existente
@app.put("/usuario/{id}", tags=["Actualizar Usuario"])
async def actualizar_usuario(id: int, usuario_actualizado: dict):
    for index in usuarios:
        if usuario["id"] == id:
            usuario.update(usuario_actualizado)
            return {"mensaje": "Usuario actualizado con éxito", "usuario": usuario}
    
    raise HTTPException(status_code=400, detail="Usuario no encontrado")

### Main FastApì ###
#Lanzar el servidor uvicorn: uvicorn main:app --reload

# Importar fastapi
from fastapi import FastAPI

app = FastAPI()


### Métodos:
# GET: Leer datos.

@app.get("/")
async def root():
    return {"message": "Hola desde FastAPI"}

@app.get("/contacto")
async def contacto():
    return {"Nombre" : "",
            "Apellido": "",
            "Teléfono": "",
            "Email"   : "" }

# Con /docs accedemos a la documentación en Swagger.
# Con /redoc accedemos a la documentacion de Redocly


# POST: Crear datos.
# PUT: Actualizar datos.
# DELETE: Borrar datos.
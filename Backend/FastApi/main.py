### Main FastApì ###

# Importar fastapi
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    
#    return { "Nombre" : "Alberto A.",
#            "Apellido": "Mariscal",
#             "Año nacimiento": "1988" }

    return {"message": "Hola desde FastAPI"}

@app.get("/contacto")
async def contacto():
    return {"Nombre" : "",
            "Apellido": "",
            "Teléfono": "",
            "Email"   : "" }

# Con /docs accedemos a la documentación en Swagger.
# Con /redoc accedemos a la documentacion de Redocly
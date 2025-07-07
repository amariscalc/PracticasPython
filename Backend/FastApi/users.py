### Users

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Entidad User
class User(BaseModel):
    id: int
    name: str
    surname: str
    web: str
    age: int

users_list = [User(id=1, name= "Alberto", surname= "Mariscal", web= "https://amariscal.com", age=35),
              User(id=2, name= "Lydia", surname= "Mariscal", web= "https://lydiamariscal.com", age=9),
              User(id=3, name= "Martina", surname= "Mariscal", web= "https://martinamariscal.com", age=6)]

@app.get("/usersJSON")
async def usersJSON():
    return [{"name": "Alberto", "surname":"Mariscal", "Web":"https://amariscal.com"},
            {"name": "Lydia", "surname":"Mariscal", "Web":"https://lydiamariscal.com"},
            {"name": "Martina", "surname":"Mariscal", "Web":"https://martinamariscal.com"}]

@app.get("/users")
async def users():
    return users_list

# Path
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)

# Al pasar el parámetro por query se especifica en el path por ejemplo /?id=1 asi estámos consultando los datos de un usuario cuya id es 1.
# Query
@app.get("/userquery/")
async def userquery(id: int):
    return search_user(id)

# Función que se encarga de buscar el usuario. Usado en las funciones asincronas "user" y "userquery"
def search_user(id: int):
    users = filter (lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return { "Error:":"El usuario no existe."}

### Post

@app.post("/user/")
async def add_user(new_user: User):
    #print (search_user(new_user.id))
    try:
        # Se comprueba si el tipo de dato que devuelve "search_user" es un Usuario (class User)
        # Si es un usuario significa que el usuario existe, 
        # si es distinto a un tipo de dato Usuario significa que el usuario no existe y por lo tanto se puede añadir.
        if(type(search_user(new_user.id))==User):
            return "El usuario ya existe"
        else:
            users_list.append(new_user)
    except:
        return "Error al introducir el usuario"
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


@app.get("/user/{id}")
async def user(id: int):
    users = filter (lambda user: user.id == id, users_list)
    return list(users)[0]
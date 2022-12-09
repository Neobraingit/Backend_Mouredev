from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI()

### Entidad user
class User(BaseModel):
    name: str   ## Aquí tipamos los datos que introducimos
    age: int

users_list = [User(name ='Marcos',age = 47 ),
         User(name = 'David', age = 42)]


@app.get('/users_jason')
async def users_jason():
   return [{'name' : 'Marcos', 'age' : 47},
           {'name' : 'David', 'age': 42}]

@app.get('/users')
async def users():
    return users_list




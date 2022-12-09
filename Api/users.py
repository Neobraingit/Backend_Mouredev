from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI()

### Entidad user
class User(BaseModel):
    id: int
    name: str   ## Aquí tipamos los datos que introducimos
    age: int

users_list = [User(id = 1, name ='Marcos',age = 47 ),
         User(id = 2, name = 'David', age = 42)]


@app.get('/users_jason')
async def users_jason():
   return [{'name' : 'Marcos', 'age' : 47},
           {'name' : 'David', 'age': 42}]
### Path
@app.get('/user/{id}')
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        print ('Error: No se ha encontrado el ususario')
### Query
@app.get('/userquery/{id}')
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        print ('Error: No se ha encontrado el ususario')




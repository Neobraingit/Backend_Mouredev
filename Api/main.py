### pip install "fastapi[all]"

from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get('/')
async def root():
   return 'Hola FastApi'


### Iniciar el server: uvicorn main:app --reload
### Documentación con Swagger: 127.0.0.1:8000/docs
### Documentación con Redocly: 127.0.0.1:8000/redoc



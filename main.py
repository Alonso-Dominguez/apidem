


from fastapi import FastAPI
from pydantic import BaseModel
import csv

app = FastAPI()

class Contacto(BaseModel):
    nombre: str
    email: str


@app.get("/")
def read_root():
    return {"Hello":"World"}


@app.get("/v1/contactos")
def get_contactos():
    datos = []
    with open('contactos.csv', 'r') as file:
        fildnames = ('nombre', 'email')
        lector = csv.DictReader(file, fildnames)
        for row in lector:
            datos.append(row)
    return datos

@app.post("/v1/contactos")
def create_contacto(contacto: Contacto):
    with open('contactos.csv', 'a', newline='') as file:
        fieldnames = ['nombre', 'email']
        escritor = csv.DictWriter(file, fieldnames=fieldnames)
        escritor.writerow({'nombre': contacto.nombre, 'email': contacto.email})
    return {"mensaje": "Contacto creado exitosamente"}

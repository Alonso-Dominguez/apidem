

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/v1/contactos")
async get_contactos():
    # TODO read contactos.csv
    # TODO JSON encode contactos 
    # TODO save in response y mostrar la URI
    response = []
    return response
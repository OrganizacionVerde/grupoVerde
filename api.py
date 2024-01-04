from fastapi import FastAPI
from entrada import obtener_datos
from pymongo import MongoClient

app = FastAPI()

# Conectar a la base de datos de MongoDB
cliente = MongoClient('localhost', 27017)
db = cliente['Entrada_de_ruedas']
coleccion = db['datos']

@app.get("/almacenar_en_mongo")
def almacenar_en_mongo():
    # Obtener datos del archivo entrada.py
    datos = obtener_datos()

    # Almacenar en la base de datos de MongoDB
    coleccion.insert_one(datos)

    return {"mensaje": "Datos almacenados en MongoDB"}
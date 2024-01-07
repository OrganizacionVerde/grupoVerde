from pymongo import MongoClient

# Conectar a la base de datos de MongoDB
cliente = MongoClient('localhost', 27017)
db = cliente['Michelin_Storage']
coleccion = db['stock']

def almacenar_en_mongo(datos):
    print(datos)
    coleccion.insert_one(document=datos)
    return {"mensaje": "Datos almacenados en MongoDB"}
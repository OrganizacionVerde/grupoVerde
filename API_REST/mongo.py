from pymongo import MongoClient

# Usuario y contraseña del cluster0 en MongoDB Atlas
user = 'dbUser'
user_password = 'dbUserPassword'

# Cadena de conexión
uri = f"mongodb+srv://{user}:{user_password}@cluster0.xiuhogh.mongodb.net/?retryWrites=true&w=majority"

# Conexión a la base de datos de MongoDB Atlas
cliente = MongoClient(uri)
db = cliente['Michelin_Storage']

def almacenar_en_mongo(datos):
    coleccion = db['stock']
    print(datos)
    coleccion.insert_one(document=datos)
    return {"mensaje": "Datos almacenados en MongoDB"}
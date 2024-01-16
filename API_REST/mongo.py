
from pymongo import MongoClient

# Usuario y contraseña del cluster0 en MongoDB Atlas
user = 'dbUser'
user_password = 'dbUserPassword'

# Cadena de conexión
uri = f"mongodb+srv://{user}:{user_password}@cluster0.xiuhogh.mongodb.net/?retryWrites=true&w=majority"

# Conexión a la base de datos de MongoDB Atlas
cliente = MongoClient(uri)
db = cliente['Michelin_Storage']

def almacenar_en_mongo(datos, coleccion='stock'):
  
    coleccion_actual = db[coleccion]
    print(datos)
    coleccion_actual.insert_one(datos)
    return {"mensaje": f'Datos almacenados en la colección "{coleccion}" de MongoDB'}

def obtener_de_mongo(condicion=None, coleccion='stock'): # Condicion es fecha de salida = 0 
    
    coleccion_actual = db[coleccion] # Coleccion actual Stock 
    datos = list(coleccion_actual.find(condicion)) if condicion else [] # Pasar los datos que cumplen la condicion 
    print("Has llegado a Mongo.py")
    return datos

def almacenar_en_mongo_historico(datos): # Almacenar el dato de salida de Stock en la coleccion Historico
   
    print("Se ha almacenado el dato en la coleccion Historico")
    return almacenar_en_mongo(datos, coleccion='historico')

def eliminar_de_mongo(datos, coleccion='stock'): # Eliminar de la coleccion Stock el dato que se acaba de introducir en Historico
   
    coleccion_actual = db[coleccion]
    for dato in datos:
        coleccion_actual.delete_one({"_id": dato["_id"]})
    
    print("Se ha eliminado de Stock y se ha pasado a Historico")

    return {"mensaje": f'Datos eliminados de la colección "{coleccion}" de MongoDB'}
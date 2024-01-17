
from pymongo import MongoClient
import random

# Usuario y contraseña del cluster0 en MongoDB Atlas
user = 'dbUser'
user_password = 'dbUserPassword'

# Cadena de conexión
uri = f"mongodb+srv://{user}:{user_password}@cluster0.xiuhogh.mongodb.net/?retryWrites=true&w=majority"

# Conexión a la base de datos de MongoDB Atlas
cliente = MongoClient(uri)
db = cliente['Michelin_Storage']

def almacenar_en_mongo(datos, coleccion='stock'):
    
    """
    Almacena un documento en mongoDB en la colección indicada

    :param datos: el documento que se quiere almacenar
    :type  datos: diccionario 

    :param coleccion: la colección en la que se quiere almacenar
    :type  coleccion: string 

    :return response: respuesta con mensaje
    :rtype  response: diccionario 

    """
  
    coleccion_actual = db[coleccion]

    coleccion_actual.insert_one(datos)
    return {"mensaje": f'Datos almacenados en la colección "{coleccion}" de MongoDB'}


def obtener_de_mongo(condicion=None, coleccion='stock'): # Condicion es fecha de salida = 0 
    
    """
    Obtiene de la colección de mongoDB indicada un documento aleatorio dependiendo de una condición

    :param condicion: condición que se quiere evaluar
    :type  condicion: boolean 

    :param coleccion: la colección de la que se quiere obtener el documento
    :type  coleccion: string

    :return dato_seleccionado: dato aleatorio que cumple la condición
    :rtype  dato_seleccionado: diccionario

    """
    coleccion_actual = db[coleccion] # Coleccion actual Stock 

    datos = list(coleccion_actual.find(condicion)) if condicion else [] # Pasar los datos que cumplen la condicion 
    
    # Si hay datos para salir, seleccionar aleatoriamente uno de ellos
    if datos:

        dato_seleccionado = random.choice(datos)

    return dato_seleccionado

def almacenar_en_mongo_historico(lote_salida): # Almacenar el dato de salida de Stock en la coleccion Historico
    
    """
    Almacena un documento en mongoDB en la colección historico

    :param lote_salida: el documento que se quiere almacenar en la colección
    :type  lote_salida: diccionario 

    :return response: respuesta con mensaje
    :rtype  response: diccionario 

    """
   
    return almacenar_en_mongo(lote_salida, coleccion='historico')

def eliminar_de_mongo(lote, coleccion='stock'): # Eliminar de la coleccion Stock el dato que se acaba de introducir en Historico
   
    coleccion_actual = db[coleccion]
    
    coleccion_actual.delete_one(lote)
    
    return {"mensaje": f'Datos eliminados de la colección "{coleccion}" de MongoDB'}
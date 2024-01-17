from fastapi import FastAPI
from modelos import Referencia
from procesamiento import procesar_referencia, procesar_lote_salida
from mongo import almacenar_en_mongo, obtener_de_mongo, almacenar_en_mongo_historico, eliminar_de_mongo

app = FastAPI() # Creación de la variable app

def guardar_respuesta(response):
    """
    Guarda la respuesta del backend FastApi en el archivo backend_response.jsonl

    :param response: respuesta del backend
    :type response: diccionario
    """

    with open('backend_response.jsonl', mode='a') as file:
        file.write(f"{str(response)}\n") 

@app.post("/generar_lote")
def generar_lote(referencia: Referencia):
    """
    Genera un lote a partir de una referencia del CSV y lo introduce en la colección stock de mongoDB

    Args:
    - `referencia` (diccionario): la referencia del CSV del que se quiere generar un lote

    Returns:
    - `response` (diccionario): respuesta con mensaje, status_code 200 y lote

    """

    lote = procesar_referencia(referencia)
    almacenar_en_mongo(lote)

    response =  {
                "mensaje":"Lote introducido con éxito",
                "status_code": 200,
                "lote":lote
            }
    
    guardar_respuesta(response)
    
    return response
       


@app.get("/salida_lote")
def salida_lote():
    lote = obtener_de_mongo(condicion={"Fecha_salida": 0}, coleccion='stock')
    eliminar_de_mongo(lote)
    lote_salida= procesar_lote_salida(lote)
    almacenar_en_mongo_historico(lote_salida)
    response = {
                "mensaje":"Lote extraido con éxito",
                "status_code": 200,
                "lote":lote_salida
            }
    
    guardar_respuesta(response)

    return response
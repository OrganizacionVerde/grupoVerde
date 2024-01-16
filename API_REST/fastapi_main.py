from fastapi import FastAPI
from modelos import Referencia
from procesamiento import procesar_referencia, procesar_lote_salida
from mongo import almacenar_en_mongo, obtener_de_mongo, almacenar_en_mongo_historico, eliminar_de_mongo

app = FastAPI()


def guardar_respuesta(response):
    with open('backend_response.jsonl', mode='a') as file:
        file.write(f"{str(response)}\n") 

@app.post("/generar_lote")
def generar_lote(referencia: Referencia):

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
                "lote":lote_salida
            }
    
    guardar_respuesta(response)

    return response
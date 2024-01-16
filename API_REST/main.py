from fastapi import FastAPI
from modelos import Referencia, Lote
from procesamiento import procesar_dimension, procesar_referencia, procesar_lote_salida
from mongo import almacenar_en_mongo, obtener_de_mongo, almacenar_en_mongo_historico, eliminar_de_mongo

app = FastAPI()

@app.post("/generar_lote")
def generar_lote(referencia: Referencia):
    lote = procesar_referencia(referencia)
    almacenar_en_mongo(lote)
    return {"mensaje":"Lote introducido con éxito",
            "lote":lote}


@app.get("/salida_lote")
def salida_lote():
    lote = obtener_de_mongo(condicion={"Fecha_salida": 0}, coleccion='stock')
    eliminar_de_mongo(lote)
    lote_salida= procesar_lote_salida(lote)
    print(lote_salida)
    almacenar_en_mongo_historico(lote_salida)
    return  {"mensaje":"Lote extraido con éxito",
            "lote":lote_salida}
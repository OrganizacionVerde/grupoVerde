from fastapi import FastAPI
from modelos import Referencia, Lote
from procesamiento import procesar_dimension, procesar_referencia
from mongo import almacenar_en_mongo

app = FastAPI()

@app.post("/generar_lote")
def generar_lote(referencia: Referencia):
    lote = procesar_referencia(referencia)
    almacenar_en_mongo(lote)
    return {"mensaje":"Lote introducido con éxito",
            "lote":lote}


from fastapi import FastAPI
from modelos import Referencia, Lote
from procesamiento import procesar_dimension, procesar_referencia

app = FastAPI()

@app.post("/generar_lote")
def generar_lote(referencia: Referencia):
    referencia_procesada = procesar_referencia(referencia)
    return referencia_procesada


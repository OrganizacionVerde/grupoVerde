from fastapi import FastAPI
from modelos import Referencia, Lote

app = FastAPI()

@app.post("/generar_lote")
def generar_lote(referencia: Referencia):
    return referencia


from fastapi import FastAPI
from modelos import Referencia

app = FastAPI()

@app.post("/generar_lote")
def generar_lote(referencia: Referencia):
    return referencia


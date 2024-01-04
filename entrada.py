import pandas as pd
import random
from fastapi import FastAPI
import json

app = FastAPI()

# Cargar datos desde el archivo Excel
excel_file = 'Excel.xlsx'
data = pd.read_excel(excel_file)

@app.get("/obtener_datos")
def obtener_datos():
    # Seleccionar aleatoriamente una fila del Excel
    fila_aleatoria = data.sample().to_dict(orient='records')[0]
    # Guardar los datos en un archivo JSON
    with open('/datos_aleatorios.json', 'w') as json_file:
        json.dump(fila_aleatoria, json_file, indent=4)

    return fila_aleatoria
import pandas as pd
from fastapi import FastAPI
import schedule
import time
from mongo import almacenar_en_mongo

app = FastAPI()

# Cargar datos desde el archivo Excel
excel_file = 'Excel.xlsx'
data = pd.read_excel(excel_file)

#@app.post("/")
def fila_aleatoria():
    # Seleccionar aleatoriamente una fila del DataFrame
    fila_aleatoria = data.sample()

    # Abrir el archivo en modo de adición y añadir la fila como un nuevo registro
    with open('entrada.jsonl', 'a') as json_file:
        fila_aleatoria.to_json(json_file, orient='records', lines=True)

    fila_dict = fila_aleatoria.to_dict(orient='records')[0]
    print(fila_dict)
    almacenar_en_mongo(fila_dict)
    return fila_dict


# Programar la ejecución de obtener_datos cada 3 segundos
schedule.every(3).seconds.do(fila_aleatoria)

# Función para ejecutar la planificación de schedule
def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    run_schedule()
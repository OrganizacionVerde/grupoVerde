import pandas as pd
from fastapi import FastAPI
import schedule
import time

app = FastAPI()

# Cargar datos desde el archivo Excel
excel_file = 'Excel.xlsx'
data = pd.read_excel(excel_file)

def fila_aleatoria():
    # Seleccionar aleatoriamente una fila del DataFrame
    fila_aleatoria = data.sample()

    # Abrir el archivo en modo de adición y añadir la fila como un nuevo registro
    with open('entrada.jsonl', 'a') as json_file:
        fila_aleatoria.to_json(json_file, orient='records', lines=True)
    return fila_aleatoria

# Programar la ejecución de obtener_datos cada 3 segundos
schedule.every(3).seconds.do(fila_aleatoria)

# Función para ejecutar la planificación de schedule
def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    run_schedule()
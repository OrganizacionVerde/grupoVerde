from fastapi import FastAPI
import pandas as pd
import json
import schedule
import time
import random

app = FastAPI()

ruedas_csv = 'CSV_Ruedas2.csv'
data = pd.read_csv(ruedas_csv)

def fila_aleatoria():

    # Seleccionar aleatoriamente una fila del CSV original
    fila_aleatoria = data.sample().iloc[0]

    # Obtener todas las dimensiones del campo "Dimension" y elegir una al azar
    dimensiones = str(fila_aleatoria['Dimension']).split(',')
    dimension_aleatoria = random.choice(dimensiones).strip()

    # Crear el formato JSON con nombres de columnas
    columnas = list(fila_aleatoria.keys())
    valores = fila_aleatoria.values.tolist()

    # Eliminar columna sin datos 
    columnas_no_deseadas = ["Unnamed: 8", "\n"]
    columnas = [columna for columna in columnas if columna not in columnas_no_deseadas]

    fila_json = dict(zip(columnas, valores))
    fila_json['Dimension'] = dimension_aleatoria

    # Convertir a JSON y escribir en el archivo
    with open('entrada.jsonl', 'a') as archivo_json:
        json.dump(fila_json, archivo_json)
        archivo_json.write('\n')

schedule.every(3).seconds.do(fila_aleatoria)

def ejecutar_programacion():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    ejecutar_programacion()

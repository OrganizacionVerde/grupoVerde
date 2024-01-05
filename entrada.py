import pandas as pd
import csv
import json
from fastapi import FastAPI
import schedule
import time

app = FastAPI()

# Cargar datos desde el archivo CSV
ruedas_csv = 'CSV_Ruedas.csv'

def leer_csv():
    filas = []
    with open(ruedas_csv, 'r', encoding='utf-8') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            filas.append(fila)
    return filas


def dividir_dimensiones():
    # Dividir los valores de la columna 'Dimension' y crear una fila por cada valor
    nuevas_filas = []
    for fila in leer_csv():
        dimension_value = fila['Dimension']

        # Verificar si el valor es un número o NaN y no está vacío
        if pd.notna(dimension_value) and ',' in dimension_value:
            dimensiones = str(dimension_value).split(',')
            for dimension in dimensiones:
                nueva_fila = fila.copy()
                nueva_fila['Dimension'] = dimension.strip()
                nuevas_filas.append(nueva_fila)
        else:
            # Si no hay múltiples valores en 'Dimension', simplemente agregar la fila
            nuevas_filas.append(fila)

    print("NUEVAS FILAS DIVIDIDAS POR DIMENSION:",nuevas_filas)
    return nuevas_filas


def fila_aleatoria():
    # Seleccionar aleatoriamente una fila de las filas divididas
    filas = dividir_dimensiones()
    fila_aleatoria = pd.DataFrame(filas).sample().iloc[0]

    # Normalizar los datos 
    fila_normalizada = fila_aleatoria.apply(lambda x: str(x) if isinstance(x, list) else x)

    # Crear manualmente el formato JSON con nombres de columnas
    columnas = fila_aleatoria.keys()
    valores = fila_normalizada.values.tolist()
    fila_json = dict(zip(columnas, valores))

    # Convertir a JSON y escribir en el archivo
    with open('entrada.jsonl', 'a') as archivo_json:
        json.dump(fila_json, archivo_json)
        archivo_json.write('\n')


# Programar la ejecución de obtener_datos cada 3 segundos
schedule.every(3).seconds.do(fila_aleatoria)

# Función para ejecutar la planificación de schedule
def ejecutar_programacion():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    ejecutar_programacion()

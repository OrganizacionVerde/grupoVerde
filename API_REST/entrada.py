import csv
import random
import requests
import pandas as pd
import io
from modelos import Referencia
from procesamiento import procesar_referencia
from mongo import almacenar_en_mongo

# URL del archivo CSV en GitHub
url = 'https://raw.githubusercontent.com/OrganizacionVerde/grupoVerde/main/CSV_Definitivo.csv'

def obtener_registro_aleatorio(url):
    # Descargar el archivo CSV desde la URL
    response = requests.get(url)
    df = pd.read_csv(io.StringIO(response.text))

    # Elegir una fila al azar del DataFrame
    registro_aleatorio = df.sample().to_dict(orient='records')[0]

    return registro_aleatorio

def procesar_y_almacenar():
    # Obtener un registro aleatorio del CSV
    registro_csv = obtener_registro_aleatorio(url)

    # Crear una instancia de Referencia a partir de la fila CSV elegida 
    referencia = Referencia(
        Nombre=registro_csv['Nombre'],
        Tipo=registro_csv['Tipo'],
        Estacion=registro_csv['Estacion'],
        Eficiencia_energetica=registro_csv['Eficiencia_energetica'],
        Capacidad_frenado=registro_csv['Capacidad_frenado_suelo_mojado'],
        Ruido_ambiental_dB=int(registro_csv['Ruido_ambiental_dB']),
        Ruido_ambiental_ondas=int(registro_csv['Ruido_ambiental_ondas']),
        Dimension=registro_csv['Dimension']
    )

    # Procesar la referencia y obtener los datos del lote
    datos_lote = procesar_referencia(referencia)

    # Almacenar en la base de datos MongoDB
    resultado_almacenamiento = almacenar_en_mongo(datos_lote)
    print(resultado_almacenamiento)

def main():
    # Llamar a la funcion principal 
    procesar_y_almacenar()

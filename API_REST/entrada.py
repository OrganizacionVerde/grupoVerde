
import requests
import pandas as pd
import io
import requests
import services

def obtener_registro_aleatorio():
    """
    Obtiene un registro aletorio del CSV de servicios.CSV_URL

    :return: Devuelve un registro aleatorio
    :rtype: diccionario 
    """

    # Descargar el archivo CSV desde la URL
    response = requests.get(services.CSV_URL)
    df = pd.read_csv(io.StringIO(response.text))

    # Elegir una fila al azar del DataFrame
    registro_aleatorio = df.sample().to_dict(orient='records')[0]

    return registro_aleatorio

def main():
    """
    Cuando entrada.py se ejecuta, llama a la función generar_lote de services.py
    """
    referencia = obtener_registro_aleatorio()
    lote = services.generar_lote(referencia)
    print(lote.text)

main()

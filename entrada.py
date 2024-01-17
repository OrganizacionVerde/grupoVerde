
import requests
import pandas as pd
import io
import requests
import services

def obtener_registro_aleatorio():
    """
    Obtiene un registro aletorio del CSV de servicios.CSV_URL

    :return: Devuelve un registro aleatorio
    :rtype:  diccionario 
    """

    # Descargar el archivo CSV desde la URL
    response = requests.get(services.CSV_URL)

    # Transformar la respuesta a un DataFrame de pandas
    df = pd.read_csv(io.StringIO(response.text))

    # Elegir una fila al azar del DataFrame
    registro_aleatorio = df.sample().to_dict(orient='records')[0]

    # Devuelve el registro aleatorio
    return registro_aleatorio

def main():
    """
    Cuando entrada.py se ejecuta, llama a la función generar_lote de services.py
    """

    # Obtiene el registro aletorio
    referencia = obtener_registro_aleatorio()

    # genera un lote con la función generar_lote
    lote = services.generar_lote(referencia)

    #imprime el lote generado
    print(f"{lote.text}\n")

main()

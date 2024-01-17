import requests
import json

# URL de la API
API_URL = "http://localhost:8000"

# URL del archivo CSV en GitHub
CSV_URL = 'https://raw.githubusercontent.com/OrganizacionVerde/grupoVerde/main/CSV_Definitivo.csv'


def generar_lote(referencia):
    """
    Llama al endpoint /generar_lote de la api con la referencia especificada

    :param referencia: la referencia a tratar
    :type  referencia: diccionario 

    :return response: respuesta de la API
    :rtype  datos_lote: diccionario 

    """
    response = requests.post(API_URL+"/generar_lote", data=json.dumps(referencia))
    return response

def salida_lote():
    """
    Llama al endpoint /salida_lote de la api

    :return response: respuesta de la API
    :rtype  datos_lote: diccionario 

    """
    response = requests.get(API_URL+"/salida_lote")
    return response




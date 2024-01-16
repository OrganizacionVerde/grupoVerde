import requests
import modelos
import json

# URL de la API
API_URL = "http://localhost:8000"

# URL del archivo CSV en GitHub
CSV_URL = 'https://raw.githubusercontent.com/OrganizacionVerde/grupoVerde/main/CSV_Definitivo.csv'

def generar_lote(referencia: modelos.Referencia):
    response = requests.post(API_URL+"/generar_lote", data=json.dumps(referencia))
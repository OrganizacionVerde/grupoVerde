# grupoVerde

## Instrucciones de uso

1. En la terminal, instalar las dependencias del archivo requirements.txt a través del comando `pip install -r requirements.txt` (se aconseja hacerlo en un entorno virtual)

2. En la terminal, en el directorio principal, ejecutar el comando `uvicorn fastapi_main:app --reload`

3. En una nueva ventana de la terminal, ejecutar el archivo python *schedule_main.py* a través del comando `/bin/python3 schedule_main.py`.
Mientras este archivo se esté ejecutando, se agregará un lote en la base de datos en MongoDB Cloud cada 3 segundos, y se sacará uno cada 5 segundos.

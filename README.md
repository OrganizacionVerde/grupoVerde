# grupoVerde
## Integrantes
* Leyre Guerra
* Javier Moreno
* Sergio Moreno

## Instrucciones de uso

1. En la terminal, instalar las dependencias del archivo requirements.txt a través del comando `pip install -r requirements.txt` (se aconseja hacerlo en un entorno virtual)

2. En la terminal, en el directorio principal, ejecutar el comando `uvicorn fastapi_main:app --reload`

3. En una nueva ventana de la terminal, ejecutar el archivo python *schedule_main.py* a través del comando `/bin/python3 schedule_main.py`.  

Mientras este archivo se esté ejecutando, se agregará un lote en la base de datos en MongoDB Cloud cada 3 segundos, y se sacará uno cada 5 segundos.  

Para acceder a la visualización en MongoDB Cloud.  

* Vista general: entrando al [siguiente enlace](https://cloud.mongodb.com/v2/659685969a83a656dde338d1#/clusters/detail/Cluster0)
* Colecciones: entrando al [siguiente enlace](https://cloud.mongodb.com/v2/659685969a83a656dde338d1#/metrics/replicaSet/659685f4c0ba965ec6fee6da/explorer)
* Vista general de las dashboards: entrando al [siguiente enlace](https://charts.mongodb.com/charts-michelin-storage-oxhtl/dashboards)
    * [Datos de stock](https://charts.mongodb.com/charts-michelin-storage-oxhtl/dashboards/2755e237-740f-4cdb-82b5-6e1948b7013e)
    * [Datos de historico](https://charts.mongodb.com/charts-michelin-storage-oxhtl/dashboards/05bd5ce3-0fba-4ce4-aac4-423dbc2d87e2)
    * [Datos para ventas](https://charts.mongodb.com/charts-michelin-storage-oxhtl/dashboards/e6304307-688e-4eb8-bb69-cdd05c68c9bc)

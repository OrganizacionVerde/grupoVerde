from datetime import datetime
import random
from API_REST.mongo import obtener_de_mongo, almacenar_en_mongo_historico, eliminar_de_mongo

def actualizar_y_mover_a_historico():
    # Obtener datos que tienen fecha de salida igual a 0 de la colección "stock"
    datos_para_salir = obtener_de_mongo(condicion={"Fecha_salida": 0}, coleccion='stock')

    # Si hay datos para salir, seleccionar aleatoriamente uno de ellos
    if datos_para_salir:
        dato_seleccionado = random.choice(datos_para_salir)

        # Actualizar la fecha de salida del dato seleccionado a la fecha actual
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dato_seleccionado["Fecha_salida"] = fecha_actual

        # Almacenar en la colección "historico"
        almacenar_en_mongo_historico(dato_seleccionado)

        # Eliminar el dato seleccionado de la colección "stock"
        eliminar_de_mongo([dato_seleccionado], coleccion='stock')

if __name__ == "__main__":
    # Ejecutar la función principal
    actualizar_y_mover_a_historico()

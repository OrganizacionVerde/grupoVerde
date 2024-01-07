from datetime import datetime
import random

# Funcion unica que recibe una DIMENSION (completa) por parametro y 
# la transforme en 6 columnas separadas y las devuelva en un diccionario

def procesar_dimension(dimension):
    # Dividir la cadena 'Dimension' en varias partes utilizando como referencia el hueco en blanco entre caracteres 
    partes = dimension.split(' ')

    # Obtener valores específicos
    ancho_perfil = partes[0]
    diametro = partes[1]
    indice_carga = partes[2]
    indice_velocidad = partes[3]

    # Dividir la columna 'Ancho_Perfil' en dos columnas separadas
    ancho, perfil = ancho_perfil.split('/')

    # Extraer los dos últimos caracteres de la columna 'Diametro' para crear nueva columna 
    diametro_interior = diametro[-2:]

    # Extraer el resto de los valores en la columna 'Estructura' para crear nueva columna "Estructura"
    estructura = diametro[:-2]

    # Crear un diccionario con los resultados
    resultado = {
        'Ancho': ancho,
        'Perfil': perfil,
        'Estructura': estructura,
        'Diametro_Interior': diametro_interior,
        'Índice de Carga': indice_carga,
        'Índice de Velocidad': indice_velocidad
    }
    print(resultado)
    return resultado

def generar_id():
   
    # Obtener la fecha y hora actual
    fecha_actual = datetime.now()

    # Formatear la fecha y hora como una cadena
    identificador = fecha_actual.strftime("%Y%m%d%H%M%S")

    return identificador
 
def asignar_cantidad():

    # Genera un número aleatorio entre 1 y 4
    random_factor = random.randint(1, 4)
    
    # Multiplica el número aleatorio por 20 para obtener paquetes de 20, 40, 60 o 80
    cantidad = random_factor * 20
    
    return cantidad

def fecha_actual():

    # Obtener la fecha y hora actual
    fecha_actual = datetime.now()

    # Formatear la fecha y hora como una cadena
    fecha_formateada = fecha_actual.strftime("%Y-%m-%d %H:%M:%S")

    return fecha_formateada

def procesar_referencia(referencia):
    
    datos_lote = {

        "_id":generar_id(),
        "Cantidad_neumaticos":asignar_cantidad(),
        "Fecha_entrada":fecha_actual(),
        "Fecha_salida":None
    }
    # Pasamos la referencia a un diccionario de python
    referencia.Dimension = procesar_dimension(referencia.Dimension)
    referencia_normalizada = referencia.dict()
    datos_lote|=referencia_normalizada
    return datos_lote
from datetime import datetime
import random
import pycountry

# Funcion unica que recibe una DIMENSION (completa) por parametro y 
# la transforme en 6 columnas separadas y las devuelva en un diccionario

def procesar_dimension(dimension):
    
    """
    Separa los valores de la dimensión indicada y devuelve un diccionario de los valores

    :param dimension: la dimensión que se quiere procesar
    :type  dimension: string 

    :return resultado: los valores de dimensión separados y procesados
    :rtype  resultado: diccionario

    """
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
    
    return resultado

def generar_id():
    
    """
    Genera y devuelve un id a través de la fecha y hora actual con formato específico

    :return identificador: id
    :rtype  identificador: int 

    """
   
    # Obtener la fecha y hora actual
    fecha_actual = datetime.now()

    # Formatear la fecha y hora como una cadena
    identificador = fecha_actual.strftime("%Y%m%d%H%M%S")

    return identificador
 
def asignar_cantidad():
    
    """
    Genera y devuelve un número aleatorio de grupo 20, 40, 60 y 80

    :return cantidad: número 20, 40, 60 y 80
    :rtype  cantidad: int

    """

    # Genera un número aleatorio entre 1 y 4
    random_factor = random.randint(1, 4)
    
    # Multiplica el número aleatorio por 20 para obtener paquetes de 20, 40, 60 o 80
    cantidad = random_factor * 20
    
    return cantidad

def fecha_actual():
    
    """
    Obitene la fecha y hora actual con formato YYYY-MM-DD HH:MM:SS

    :return fecha_formateada: fecha y hora actual
    :rtype  fecha_formateada: datetype 

    """

    # Obtener la fecha y hora actual
    fecha_actual = datetime.now()

    # Formatear la fecha y hora como una cadena
    fecha_formateada = fecha_actual.strftime("%Y-%m-%d %H:%M:%S")

    return fecha_formateada

def procesar_referencia(referencia):
    
    """
    Procesa la referencia obtenida y agrega datos _id, Cantidad_neumaticos, Fecha_entrada y Fecha_salida 
    para crear un documento de tipo datos_lote

    :param referencia: la referencia a tratar
    :type  referencia: diccionario 

    :return datos_lote: documento datos_lote creados
    :rtype  datos_lote: diccionario 

    """
    
    datos_lote = {

        "_id":generar_id(),
        "Cantidad_neumaticos":asignar_cantidad(),
        "Fecha_entrada":fecha_actual(),
        "Fecha_salida": 0
    }
    # Pasamos la referencia a un diccionario de python
    referencia.Dimension = procesar_dimension(referencia.Dimension)
    referencia_normalizada = referencia.dict()
    datos_lote|=referencia_normalizada
    return datos_lote

def procesar_lote_salida(lote):
    
    """
    Procesa el lote obtenido y agrega Fecha_salida, Cliente y Pais_destino
    para crear un documento de tipo lote_salida

    :param lote: el lote a tratar
    :type  lote: diccionario 

    :return lote: documento lote creados
    :rtype  lote: diccionario 

    """

    clientes = ['MercedesBenz', 'Porsche', 'Audi', 'BMW', 'Hyundai', 'Fiat', 'Toyota', 'Nissan', 'Lamborghini', 'Ferrari', 'Bugatti', 'Honda', 'Opel', 'Volvo', 'Peugeot', 'Citroën', 'Renoult', 'Seat', 'Cupra', 'Ford', 'Chevrolet', 'Norauto', 'Feu_Vert', 'Midas','Aurgi']
    datos_lote_salida = {

        "Fecha_salida": fecha_actual(),
        "Cliente": random.choice(clientes),
        "Pais_destino": generar_pais_aleatorio()

    }

    lote|=datos_lote_salida

    return lote

def generar_pais_aleatorio():
    
    """
    Genera un diccionario con datos alpha_2, alpha_3 y name de un país aleatorio 

    :return pais_aleatorio: 
    :rtype  datos_lote: diccionario 

    """
    paises = [{'alpha_2': pais.alpha_2, 
               'alpha_3': pais.alpha_3, 
               'name': pais.name
               } for pais in pycountry.countries]

    
    pais_aleatorio = random.choice(paises)

    return pais_aleatorio

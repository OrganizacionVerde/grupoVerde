
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

    # Dividir la columna 'Ancho_Perfil' en dos partes
    ancho, perfil = ancho_perfil.split('/')

    # Extraer los dos últimos caracteres de la columna 'Diametro'
    diametro_interior = diametro[-2:]

    # Extraer el resto de los valores en la columna 'Estructura'
    estructura = diametro[:-2]

    # Crear un diccionario con los resultados
    resultado = {
        #'Dimension_Completa': dimension,
        #'Ancho_Perfil': ancho_perfil,
        #'Diametro': diametro,
        'Ancho': ancho,
        'Perfil': perfil,
        'Estructura': estructura,
        'Diametro_Interior': diametro_interior,
        'Índice de Carga': indice_carga,
        'Índice de Velocidad': indice_velocidad
    }
    print(resultado)
    return resultado

def procesar_referencia(referencia):

    referencia.Dimension = procesar_dimension(referencia.Dimension)
    print(referencia)
    return referencia
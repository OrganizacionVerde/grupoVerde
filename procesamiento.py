import pandas as pd

# Esto tiene que ser una funcion unica que reciba una DIMENSION (completa) por parametro y 
# la transforme en 6 columnas separadas y las devuelva en un diccionario, pero sin usar pandas,
# simplemente tratandolo como String 

# Cargar el DataFrame desde el archivo CSV
df = pd.read_csv('CSV_Definitivo.csv')

# Dividir la columna 'Dimension' en varias columnas
split_columns = df['Dimension'].str.split(expand=True)
num_expected_columns = 4

# Asignar las nuevas columnas al DataFrame
df[['Ancho_Perfil', 'Diametro', 'Índice de Carga', 'Índice de Velocidad']] = split_columns

# Dividir la columna 'Ancho_Perfil' en dos columnas
split_columns_2 = df['Ancho_Perfil'].str.split('/', expand=True)
num_expected_columns_2 = 2

# Asignar las nuevas columnas al DataFrame
df[['Ancho', 'Perfil']] = split_columns_2

# Extraer los dos últimos caracteres de la columna 'Diametro'
df['Diametro_Interior'] = df['Diametro'].str[-2:]

# Extraer el resto de los valores en la columna 'Estructura'
df['Estructura'] = df['Diametro'].str[:-2]

# Eliminar columnas innecesarias
df.drop(['Dimension', 'Ancho_Perfil', 'Diametro'], axis=1, inplace=True)

# Reordenar las columnas
orden_columnas = [
    'Nombre', 'Tipo', 'Estacion', 'Eficiencia_energetica', 'Capacidad_frenado_suelo_mojado',
    'Ruido_ambiental_dB', 'Ruido_ambiental_ondas', 'Ancho', 'Perfil', 'Estructura',
    'Diametro_Interior', 'Índice de Carga', 'Índice de Velocidad'
]

df = df[orden_columnas]

# Mostrar el DataFrame resultante
print(df)

# Guardar el DataFrame resultante en un nuevo archivo CSV
df.to_csv('CSV_Final_Nuevo.csv', index=False)


import pandas as pd     
import numpy as np 
# Obtener los nombres de las columnas
arr = pd.DataFrame({'a2a': [4, 2, 1, 3], 'b32b': [4, 2, 1, 3]})

columnas = arr.columns.tolist()

# Crear una lista con los nuevos nombres de columnas
nuevas_columnas = [columna.upper() for columna in columnas]

# Renombrar las columnas en el dataframe
arr.columns = nuevas_columnas

print(arr)
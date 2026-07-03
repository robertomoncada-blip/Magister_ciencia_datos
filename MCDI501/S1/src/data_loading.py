
# src/data_loading.py
"""
Módulo asociado a la carga de datos desde archivos CSV.

Expone la función cargar_datos, que lee un archivo CSV
desde una ruta especificada y retorna un DataFrame de pandas, 
manejando de forma controlada los errores de archivo no encontrado.
"""


import pandas as pd

def cargar_datos(ruta):
    """
    Carga un archivo CSV y retorna un DataFrame
    """
    try:
        df = pd.read_csv(ruta)
    except FileNotFoundError:
        print(
            f"No se encontro el archivo '{ruta}'. "
            "Verifica que el CSV este en la misma carpeta del notebook."
        )
        return None
    print(f"Datos cargados: {df.shape[0]} filas y {df.shape[1]} columnas.")
    return df

# scripts/cargar_datos.py
import pandas as pd

def cargar_datos(ruta_archivo):
    datos = pd.read_csv(ruta_archivo)
    return datos

if __name__ == "__main__":
    ruta_archivo = '../data/ventas.csv'
    datos = cargar_datos(ruta_archivo)
    print(datos.head())

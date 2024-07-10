# scripts/analizar_datos.py
import pandas as pd

def analizar_datos(datos):
    resumen = datos.groupby('producto').agg({'ventas': 'sum', 'cantidad': 'sum'})
    return resumen

if __name__ == "__main__":
    from cargar_datos import cargar_datos

    ruta_archivo = '../data/ventas.csv'
    datos = cargar_datos(ruta_archivo)
    resumen = analizar_datos(datos)
    print(resumen)

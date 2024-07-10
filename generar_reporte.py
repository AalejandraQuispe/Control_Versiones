# scripts/generar_reporte.py
import pandas as pd

def generar_reporte(resumen, ruta_reporte):
    resumen.to_csv(ruta_reporte, index=True)
    print(f'Reporte generado: {ruta_reporte}')

if __name__ == "__main__":
    from cargar_datos import cargar_datos
    from analizar_datos import analizar_datos

    ruta_archivo = '../data/ventas.csv'
    ruta_reporte = '../data/reporte_ventas.csv'
    datos = cargar_datos(ruta_archivo)
    resumen = analizar_datos(datos)
    generar_reporte(resumen, ruta_reporte)


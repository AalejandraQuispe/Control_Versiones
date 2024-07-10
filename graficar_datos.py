# scripts/graficar_datos.py
import pandas as pd
import matplotlib.pyplot as plt

def graficar_datos(resumen, ruta_grafico):
    resumen.plot(kind='bar')
    plt.title('Ventas por Producto')
    plt.xlabel('Producto')
    plt.ylabel('Ventas')
    plt.savefig(ruta_grafico)
    plt.close()
    print(f'Gráfico generado: {ruta_grafico}')

if __name__ == "__main__":
    from cargar_datos import cargar_datos
    from analizar_datos import analizar_datos

    ruta_archivo = '../data/ventas.csv'
    ruta_grafico = '../data/grafico_ventas.png'
    datos = cargar_datos(ruta_archivo)
    resumen = analizar_datos(datos)
    graficar_datos(resumen, ruta_grafico)


# scripts/enviar_reporte.py
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def enviar_reporte(ruta_reporte, ruta_grafico, destinatario):
    remitente = 'tu_email@gmail.com'
    password = 'tu_contraseña'
    
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje['Subject'] = 'Reporte de Ventas'

    cuerpo = 'Adjunto encontrarás el reporte de ventas y el gráfico correspondiente.'
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    # Adjuntar reporte
    adjunto_reporte = open(ruta_reporte, 'rb')
    parte_reporte = MIMEBase('application', 'octet-stream')
    parte_reporte.set_payload(adjunto_reporte.read())
    encoders.encode_base64(parte_reporte)
    parte_reporte.add_header('Content-Disposition', f'attachment; filename= {ruta_reporte}')
    mensaje.attach(parte_reporte)

    # Adjuntar gráfico
    adjunto_grafico = open(ruta_grafico, 'rb')
    parte_grafico = MIMEBase('application', 'octet-stream')
    parte_grafico.set_payload(adjunto_grafico.read())
    encoders.encode_base64(parte_grafico)
    parte_grafico.add_header('Content-Disposition', f'attachment; filename= {ruta_grafico}')
    mensaje.attach(parte_grafico)

    # Enviar correo
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login(remitente, password)
    texto = mensaje.as_string()
    servidor.sendmail(remitente, destinatario, texto)
    servidor.quit()

    print(f'Correo enviado a {destinatario}')

if __name__ == "__main__":
    from cargar_datos import cargar_datos
    from analizar_datos import analizar_datos
    from generar_reporte import generar_reporte
    from graficar_datos import graficar_datos

    ruta_archivo = '../data/ventas.csv'
    ruta_reporte = '../data/reporte_ventas.csv'
    ruta_grafico = '../data/grafico_ventas.png'
    destinatario = 'destinatario@ejemplo.com'

    datos = cargar_datos(ruta_archivo)
    resumen = analizar_datos(datos)
    generar_reporte(resumen, ruta_reporte)
    graficar_datos(resumen, ruta_grafico)
    enviar_reporte(ruta_reporte, ruta_grafico, destinatario)

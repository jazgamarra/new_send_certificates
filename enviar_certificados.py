import os
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication 
import smtplib

# RUTAS 
carpeta_archivos = r'/home/.../carpeta_certificados' # modificar path 
ruta_csv = r'/home/.../lista_certificados.csv' # modificar path 

# CONFIGURACIONES EMAIL 
correo_emisor = 'jazgamarra@example' # modificar email 
password_emisor = 'password123' # modificar contrasenha 
asunto_correo = 'Certificado - Cursos de Verano'
cuerpo_correo = '''¡Muchas gracias por participar de los Cursos de Verano! Adjuntamos tu certificado de participación. '''

correspondencia_nombres = {} # dios me perdone 

def enviar_correo(correo_destinatario, archivo):
    msg = MIMEMultipart()
    msg['From'] = correo_emisor
    msg['To'] = correo_destinatario
    msg['Subject'] = asunto_correo

    msg.attach(MIMEText(cuerpo_correo, 'plain')) 

    with open(archivo, "rb") as f:
        adjunto = MIMEApplication(f.read(), _subtype="pdf")
        adjunto.add_header('Content-Disposition', 'attachment', filename=os.path.basename(archivo))
        msg.attach(adjunto)

    # Enviar el correo
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(correo_emisor, password_emisor)
    server.sendmail(correo_emisor, correo_destinatario, msg.as_string())
    server.quit()

def generar_diccionario_correos():
    with open(ruta_csv, 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        for fila in lector_csv:
            if len(fila) >= 2:
                nombre_nuevo, nombre_actual = fila
                correspondencia_nombres[nombre_actual] = nombre_nuevo

def main (): 
    # Obtener la lista de archivos pdf en la carpeta
    archivos_pdf = [archivo for archivo in os.listdir(carpeta_archivos) if archivo.endswith('.pdf')]

    # Enviar cada archivo a la dirección de correo correspondiente
    for archivo in archivos_pdf:
        
        correo_destinatario = correspondencia_nombres[archivo[:-4]]
        ruta_archivo = os.path.join(carpeta_archivos, archivo)
        enviar_correo(correo_destinatario, ruta_archivo)
        print(f'Archivo {archivo} enviado a {correo_destinatario} correctamente.')
        

generar_diccionario_correos()
main()
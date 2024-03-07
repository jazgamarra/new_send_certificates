# Automatizacion para la entrega de certificados de los cursos estacionales 

## Organizacion del proyecto 
- En la carpeta `carpeta_certificados` se almacenan los certificados en formato pdf, existiendo un archivo por cada persona. 
- En el archivo `lista_certificados.csv` se tiene una lista que parea el nombre de archivo con el correo electronico de la persona a quien corresponde dicho certificado. Este archivo puede generarse a partir de la planilla de control, si existiese. 
- Para ejecutar `enviar_certificados.py`, se deben modificar los datos de acceso al correo emisor, el asunto y cuerpo del correo. 


## Creacion de certificados 
Personalmente encontre dos maneras de generar certificados rapido a partir de una lista en csv de los participantes: Pueden generarse en canva con la opcion "bulk create", o en word con la opcion "enviar correspondencia". Es necesario tener los certificados hechos antes de ejecutar el script, ya que este solo se se encarga de hacer llegar cada archivo a la persona que corresponde a traves del correo electronico. 

--- 
jazgamarra@gmail.com 
07/03/2024

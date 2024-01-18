import csv
import os
import PySimpleGUI as sg

from UNLPImage.configuracion.constante import DIR_PROYECTO

def crear_archivo_csv(datos,tags,descrip):

    """
    Crea un archivo CSV y escribe los datos de la imagen junto con los tags y descripcion asociados.

    Parametros:
    - datos: Un diccionario que contiene los datos de la imagen, como la ruta, resolucion, tamaño, tipo, etc.
    - tags: Una lista de tags asociados a la imagen.
    - descrip: La descripcion de la imagen.

    """

    # Nombres de las columnas para el archivo CSV
    nombres_columnas = ["ruta", "descripcion", "resolucion", "size", "tipo", "ultimo_perfil", "fecha_actualizacion", "tags"]

    try:
        ruta = os.path.join('UNLPImage', 'archivos', 'datos_imagenes.csv')

        # Verifica si el archivo existe
        archivo_existe = os.path.exists(ruta)

        with open(ruta, mode='a', newline='') as archivo_csv:
            writer = csv.writer(archivo_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            # Escribe los nombres de las columnas si el archivo es recién creado
            if not archivo_existe:
                writer.writerow(nombres_columnas)

            ruta = os.path.relpath(datos['ruta'], DIR_PROYECTO).replace(os.path.sep,"/")

            if len(tags) > 0:
                tags = ','.join(tags)
            else:
                tags = ""
            writer.writerow([
                ruta,
                descrip,
                datos['resolucion'],
                datos['size'],
                datos['tipo'],
                datos['ultimo_perfil'],
                datos['fecha_actualizacion'],
                tags
            ])

    except PermissionError:
        sg.popup_error("No se tienen permisos para acceder al archivo CSV.")
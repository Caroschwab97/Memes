import csv
import os
import PySimpleGUI as sg
from datetime import date

def agregar_tag(ruta_imagen, nuevo_tag, nick):

    """
    Agrega un nuevo tag a un archivo de imagen en un archivo CSV de datos de imagenes.

    Parametros:
    - ruta_imagen (str): Ruta del archivo de imagen.
    - nuevo_tag (str): Nuevo tag a agregar.
    - nick (str): Nick del usuario.

    """

    ruta_archivo = os.path.join('UNLPImage', 'archivos', 'datos_imagenes.csv')
    nombre_archivo = os.path.basename(ruta_imagen)
    datos_csv = []

    try:
        with open(ruta_archivo, 'r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            for fila in lector_csv:
                if os.path.basename(fila[0]) == nombre_archivo:
                    fila[7] = ','.join(fila[7].split(',') + [nuevo_tag])
                    fila[5] = nick
                    fila[6] = date.today().strftime("%Y-%m-%d")
                datos_csv.append(fila)

        with open(ruta_archivo, 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerows(datos_csv)
    except (FileNotFoundError):
        pass
    except PermissionError:
        sg.popup_error("No se tienen permisos para acceder al archivo CSV.")
        return
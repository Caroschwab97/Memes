import csv
import os
import PySimpleGUI as sg
from datetime import date

def eliminar_tag(ruta_imagen, tag_a_eliminar, nick):
    ruta_archivo = os.path.join('UNLPImage', 'archivos', 'datos_imagenes.csv')
    nombre_archivo = os.path.basename(ruta_imagen)

    try:
        with open(ruta_archivo, 'r', newline='') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            datos_csv = list(lector_csv)
            for fila in datos_csv:
                nombre_fila = os.path.basename(fila[0])
                if nombre_fila == nombre_archivo:
                    lista_tags = fila[7].split(',')
                    if tag_a_eliminar in lista_tags:
                        lista_tags.remove(tag_a_eliminar)
                    fila[7] = ','.join(lista_tags)
                    fila[5] = nick
                    fila[6] = date.today().strftime('%Y-%m-%d')

        with open(ruta_archivo, 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerows(datos_csv)

    except (FileNotFoundError):
        sg.popup_error("No se encontro el archivo, no pudo eliminarse el tag")
    except PermissionError:
        sg.popup_error("No se tienen permisos para acceder al archivo CSV, no pudo eliminarse el tag")
        return
import csv
import os
from PIL import Image
import PySimpleGUI as sg

from datetime import date

def guardar_imagen_actualizada(ruta_nueva, nick):

    """
    Actualiza los datos de una imagen en un archivo CSV con la ruta, tamaño, nombre de usuario y fecha actualizados.

    Parametros:
    - ruta_nueva: La ruta de la nueva imagen.
    - nick: El nombre de usuario.

    """

    datos_csv = []
    nombre_archivo = os.path.basename(ruta_nueva)
    ruta_archivo = os.path.join('UNLPImage', 'archivos', 'datos_imagenes.csv')

    try:
        with open(ruta_archivo, 'r', newline='') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            for fila in lector_csv:
                nombre_fila = os.path.basename(fila[0])
                if nombre_fila == nombre_archivo:
                    fila[3] = os.path.getsize(ruta_nueva)
                    fila[5] = nick
                    fila[6] = date.today().strftime('%Y-%m-%d')
                datos_csv.append(fila)

        with open(ruta_archivo, 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerows(datos_csv)

    except FileNotFoundError:
        sg.popup_error("No se encontró el archivo CSV.")
        return

    except PermissionError:
        sg.popup_error("No se tienen permisos para acceder al archivo CSV.")
        return


def actualizar_tamanio(file, nuevo_tamano_bytes,nick):

    """
    Actualiza el tamaño de una imagen en bytes y guarda la imagen redimensionada en una nueva ubicación.

    Parametros:
    - file: La ruta del archivo de imagen.
    - nuevo_tamano_bytes: El nuevo tamaño en bytes deseado para la imagen.
    - nick: El nombre de usuario.

    """

    with open(file, 'rb') as image_file:
        image_data = image_file.read()

    # Abre la imagen usando Pillow (PIL)
    img = Image.open(file)

    # Calcula el tamaño deseado en pixeles en función del nuevo tamaño en bytes
    tamano_actual_bytes = os.path.getsize(file)
    nuevo_tamano_bytes = int(nuevo_tamano_bytes)  # Convertir a integer
    factor_escala = (nuevo_tamano_bytes / tamano_actual_bytes) ** 0.6
    # Se obtiene un tamaño muy cercano al deseado
    nuevo_tamano_pixels = round(factor_escala * img.size[0]), round(factor_escala * img.size[1])

    # Cambia el tamaño de la imagen
    img_resized = img.resize(nuevo_tamano_pixels)

    nombre = os.path.basename(file)
    extension = os.path.splitext(file)[1]
    ruta_nueva = os.path.join('UNLPImage', 'imagenes', 'imagenes_collages', f"{nombre}")

    guardar_imagen_actualizada(ruta_nueva,nick)  

    # Guarda la imagen redimensionada
    img_resized.save(ruta_nueva)
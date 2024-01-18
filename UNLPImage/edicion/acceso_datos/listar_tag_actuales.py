import PySimpleGUI as sg
import os
import csv

def recuperar_tags(ruta_imagen):

    """
    Recupera los tags asociados a una imagen a partir de un archivo CSV.

    Parametros:
    - ruta_imagen: La ruta de la imagen.

    Retorna:
    - lista_extraida: Una lista de tags asociados a la imagen.

    """

    try:
        nombre_archivo = os.path.basename(ruta_imagen)
        ruta_archivo = os.path.join('UNLPImage', 'archivos', 'datos_imagenes.csv')
        with open(ruta_archivo, 'r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            for fila in lector_csv:
                nombre_fila = os.path.basename(fila[0])
                if nombre_fila == nombre_archivo:
                    # La lista de tags se encuentra en la posición 7 de la fila
                    lista_extraida = fila[7].split(',')
                    return lista_extraida
    except Exception as e:
        mensaje_error = f"Error al recuperar los tags: {str(e)}"
        sg.popup_error(mensaje_error)
    return []
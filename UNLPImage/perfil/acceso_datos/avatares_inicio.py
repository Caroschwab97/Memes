import PySimpleGUI as sg
import os
import json

from UNLPImage.perfil.constantes.constante import ruta_archivo

def avatares(): 

    """
    Carga los avatares desde un archivo JSON y los muestra como botones en una interfaz grafica.
    
    Returns:
        list: Una lista de botones que representan los avatares cargados.
    """
    
    try:

        # Leer el archivo json
        with open(ruta_archivo, 'r', encoding='utf-8') as jsonfile:
            data = json.load(jsonfile)
            dicc = {}
            # Definir una función para cargar la imagen a partir de la ruta
            def load_image(avatar):
                try:
                    with open(avatar, 'rb') as image_file:
                        return image_file.read()
                except FileNotFoundError:
                    sg.popup_error(f"Error al cargar el avatar {avatar}")
                    return None  # Retorna None si la imagen no se encuentra
            # Utilizar map para aplicar la función a cada elemento en data y construir el diccionario
            dicc = dict(map(lambda row: (row['nick'], load_image(row['avatar'])), data))
    except FileNotFoundError:
        sg.popup_error("No se encontró el archivo perfiles.json.")
        return []
    
    avatares = [
                [sg.Button('', image_data=dicc[ruta], image_size=(70, 70), key=ruta)]
                for ruta in dicc.keys() if ruta in dicc and dicc[ruta] is not None
               ]

    return avatares
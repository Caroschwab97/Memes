import os
import json

from UNLPImage.perfil.constantes.constante import ruta_archivo

def cargar_datos():

    """
    Lee los datos de un archivo JSON y devuelve una lista de perfiles.

    Returns:
        list: Una lista de perfiles cargados desde el archivo JSON.
    """

    # Lee los datos del archivo JSON y devuelve una lista de perfiles
    try:

        with open(ruta_archivo) as archivo:
            datos = json.load(archivo)
        return datos
    except FileNotFoundError:
        # Manejar el error si el archivo no se encuentra
        print("Error: archivo no encontrado.")
        return []


def buscar_perfil(nick):

    '''
    Busca y devuelve el perfil correspondiente al perfil actual.
    Returns:
        dict or None: Diccionario que representa el perfil correspondiente al perfil actual.
        Si no se encuentra ningún perfil, se devuelve None.
    '''

    # Carga los datos y crea la GUI
    datos = cargar_datos()

    perfil = next((p for p in datos if p['nick'] == nick), None)

    return perfil
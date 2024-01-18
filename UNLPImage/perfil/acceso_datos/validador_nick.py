import json
import os

from UNLPImage.perfil.constantes.constante import ruta_archivo

def validar_nick(nick):

    """
    Valida si un nick ya existe en el archivo de perfiles.

    Args:
        nick (str): El nick a validar.

    Raises:
        ValueError: Si el nick ya existe en el archivo de perfiles.

    """

    with open(ruta_archivo, 'r') as file:
        lines = file.readlines()
        if any(nick in line for line in lines):
            raise ValueError(f"El nick '{nick}' ya existe en el archivo de perfiles.")
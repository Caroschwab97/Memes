import os
import json

from UNLPImage.perfil.constantes.constante import ruta_archivo

def guardar_datos(dato,nick):

    '''
    Actualiza y guarda los datos del perfil actual en el archivo JSON.

    Args:
        dato (list): Lista de datos del perfil actualizado en el siguiente orden:
                     [nombre, edad, genero, avatar]

    Returns:
        None
    '''

    with open(ruta_archivo, 'r') as archivo:
        datos = json.load(archivo)
    perfil = next((p for p in datos if p['nick'] == nick), None)
    if perfil:
        perfil['nombre'] = dato[0]
        perfil['edad'] = dato[1]
        perfil['genero'] = dato[2]
        perfil['avatar'] = dato[3]
    
    # Escribe los datos actualizados en el archivo JSON
    with open(ruta_archivo, 'w') as archivo:
        json.dump(datos, archivo, indent=4)
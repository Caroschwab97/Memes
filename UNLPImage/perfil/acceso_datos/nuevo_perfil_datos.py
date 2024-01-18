import json
import os

from UNLPImage.configuracion.constante import DIR_PROYECTO
from UNLPImage.perfil.constantes.constante import ruta_archivo

def guardar_perfil(datos):

    '''
    Guarda un perfil de usuario en el archivo "perfiles.json" con los datos proporcionados.
    Args:
        datos (list): Una lista que contiene los datos del perfil de usuario en el siguiente orden:
        nick, nombre, edad, género y avatar.
    Returns:
        None
    '''

    # Verificar si el archivo JSON existe
    if not os.path.exists(ruta_archivo):
        perfiles = []
    else:
        # Si el archivo ya existe, cargar los perfiles existentes
        with open(ruta_archivo) as f:
            perfiles = json.load(f)
    with open(ruta_archivo, 'w') as archivo_json:
        avatar = os.path.relpath(datos[4], DIR_PROYECTO).replace(os.path.sep,"/")
        # Convertir los datos a un diccionario
        perfil = {'nick': datos[0], 'nombre': datos[1], 'edad': datos[2], 'genero': datos[3], 'avatar': avatar}
        # Agregar el perfil a la lista de perfiles
        perfiles.append(perfil)
        # Escribir la lista de perfiles en el archivo JSON
        json.dump(perfiles, archivo_json, indent=4)


def guardo_imagen(imagen,nick):

    """
    Guarda una imagen en el sistema utilizando el nombre de usuario (nick) proporcionado.
    Args:
        imagen (str): La ruta de la imagen a guardar.
        nick (str): El nombre de usuario asociado a la imagen.
    Returns:
        str: La ruta de la nueva imagen guardada.
    """

    with open(imagen, 'rb') as image_file:
        image_data = image_file.read()
      
    #nombre_imagen = os.path.basename(imagen)
    ruta_nueva = os.path.join('UNLPImage', 'imagenes', 'img_sistema', f"image-{nick}.png")
    with open(ruta_nueva, 'wb') as new_image_file:
        new_image_file.write(image_data)

    return ruta_nueva
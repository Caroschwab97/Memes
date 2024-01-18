import json
import os

from UNLPImage.perfil.constantes.constante import ruta_archivo

def baja_perfil(nick):

    """
    Elimina un perfil de usuario del archivo JSON de perfiles.
    Parameters:
        nick (str): El nickname del perfil que se desea eliminar.
    Returns:
        bool: True si el perfil se eliminó correctamente.
    """

    # Paso 1: Leer el archivo JSON y cargar su contenido
    with open(ruta_archivo, 'r') as archivo_json:
        data = json.load(archivo_json)

    # Paso 2: Buscar el perfil correspondiente al nick recibido y borrarlo
    for registro in data:
        if nick in registro.values():
            data.remove(registro)
            ruta_img = os.path.join('UNLPImage', 'imagenes', 'img_sistema', f"image-{nick}.png") 
            # Eliminar la imagen del perfil borrado
            if os.path.exists(ruta_img):
                os.remove(ruta_img)      

            # Paso 3: Escribir la estructura de datos modificada en el archivo JSON
            with open(ruta_archivo, 'w') as archivo_json:
                json.dump(data, archivo_json, indent=4)
               
            return True
            break
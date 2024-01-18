import os
import json

from UNLPImage.configuracion.constante import DIR_PROYECTO

def cargar_configuracion():

    """
    Carga la configuración desde un archivo JSON.

    Intenta abrir y cargar el archivo de configuracion "configuracion.json" ubicado en el directorio
    "UNLPImage/archivos".
    Si el archivo no se encuentra o no es un archivo JSON valido, retorna un diccionario con valores
    predeterminados.

    Returns:
        dict: Diccionario que contiene la configuración cargada desde el archivo JSON o valores predeterminados.

    """
    
    try:
        # Construye la ruta de archivo utilizando os.path.join()
        ruta_archivo = os.path.join('UNLPImage', 'archivos', 'configuracion.json')
        with open(ruta_archivo, "r") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return {
                "imagenes": "",
                "collages": "",
                "memes": ""
                }
        

def actualizar_configuracion(datos):

    """
    Actualiza la configuracion con nuevos datos y guarda los cambios en un archivo JSON.

    Parametros:
        datos (dict): Diccionario que contiene los nuevos datos de configuracion. Las claves representan
        los nombres de los campos de configuracion, y los valores son las rutas relativas a 'DIR_PROYECTO'
        que se actualizaran en la configuracion existente.
    """

    configuracion_existente = cargar_configuracion()

    configuracion_existente.update({k: os.path.relpath(v, DIR_PROYECTO).replace(os.path.sep,"/") for k, v in datos.items() if v is not None})

    # Construye la ruta de archivo utilizando os.path.join()
    ruta_archivo = os.path.join('UNLPImage', 'archivos', 'configuracion.json')

    with open(ruta_archivo, "w") as archivo:
        json.dump(configuracion_existente, archivo, indent=4)

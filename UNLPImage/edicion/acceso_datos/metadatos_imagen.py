import PySimpleGUI as sg
from datetime import date
from PIL import Image
import os

def obtener_metadatos_imagen(ruta,nick):
    try:
        
        metadatos = {}
        imagen = Image.open(ruta)
        #ruta relativa de la imagen
        metadatos['ruta'] = ruta

        #resolución de la imagen
        metadatos['resolucion'] = imagen.size
        
        #tamaño de la imagen
        metadatos['size'] = os.path.getsize(ruta)

        #tipo de la imagen
        metadatos['tipo'] = imagen.format

        # Obtiene el último perfil que actualizó y la fecha de última actualización
        metadatos['ultimo_perfil'] = nick
        fecha = date.today()
        metadatos['fecha_actualizacion'] = fecha
        imagen.close()
        return metadatos     
    except IOError:
        sg.popup("Error al abrir la imagen")
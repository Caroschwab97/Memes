import io
import json
import os 
import PIL
from PIL import Image, ImageDraw, ImageFont
import PySimpleGUI as sg
import textwrap

from UNLPImage.edicion.acceso_datos.coordenadas_cajas import obtener_coordenadas, desempaquetar_coordendas, tamaño_contenedor


def apertura_archivo():
    ruta_archivo = os.path.join('UNLPImage', 'archivos', 'imagenes_memes.json')
    try:
        with open(ruta_archivo,'r') as archivo_memes:
            datos_leidos = json.load(archivo_memes)
        return datos_leidos
    except FileNotFoundError:
        sg.Popup('El archivo no existe')
        return[]

def _imagenes_memes():

    """
    Genera una lista de botones con las imagenes que se utilizaran para hacer memes a partir de los 
    archivos de imágenes en la carpeta     'UNLPImage/imagenes/memes'.

    Retorna:
    - memes: Una lista de botones con las imagenes permitidas para realizar un meme.

    """
    memes = []
    datos = apertura_archivo()
    i = 0
    for nombre_img in datos:
        imagen = os.path.join('UNLPImage', 'imagenes', 'memes', f'{nombre_img["image"]}')
        meme = [sg.Button(image_filename=imagen,image_size=(100, 100), key=f'{nombre_img["image"]}')]
        memes.append(meme)
        i += 1
    return memes
    
def obtener_cant_boxes(img_seleccionada):
    """
    Funcion que permite obtener la cantidad de cuadros de texto que tiene la plantilla para el meme.
    
    Parametros:
    - img_seleccionada: plantilla que fue elegida para el meme
    """
    datos = apertura_archivo()
    img_sel = os.path.basename(img_seleccionada)
    for line in datos:
        if img_sel == line["image"]:
            return line["cant_boxes"]

def generar_inputs(img_seleccionada):
    """
    Genera los inputs de texto para cada una de las imagenes, dependiendo de la cantidad
    de text_boxes que tengan..

    Parametros:
        - img_seleccionada: es la imagen que se convertirá en meme
    Retorna:
        - una lista con todos los inputs
    """
    datos = apertura_archivo()
    text_boxes = []
    img_sel = os.path.basename(img_seleccionada)
    for line in datos:
        if img_sel == line["image"]:
            for i in range(obtener_cant_boxes(img_seleccionada)):
                text_box = [sg.Input(key=f'-TEXTO{i}-', size=(40,2))]
                text_boxes.append(text_box)
    return text_boxes
    
def _guardar_meme(nick,imagen,lista,fuente_texto,tipo_img,nombre_meme):
    """
    Permite guardar el meme generado dentro de una carpeta seleccionada por el usuario, el path 
    de dicha carpeta se encuentra en el archivo 'configuracion.json'

    Parametros:
        - nick: en nombre del usuario
        - imagen: meme editado proveniente de edicion_meme
        - lista: contiene los valores de todos los inputs
        - fuente_texto: el tipo de fuente que se usara para el texto
        - tipo_img: puede ser png o jpg define el tipo de archivo de imagen en el que se guardará el meme
        - nombre_meme: nombre asignado por el usuario para el meme creado
    """
    archivo_config = os.path.join('UNLPImage', 'archivos', 'configuracion.json')
    with open(archivo_config, 'r') as archivo:
        carpetas = json.load(archivo)
        
    # Obtener la ruta de la carpeta desde el archivo 'configuracion.json'
    ruta_carpeta = carpetas.get("memes")
    boxes = obtener_cant_boxes(imagen)
    datos_archivo = apertura_archivo()

    coordenadas_text_boxes = obtener_coordenadas(imagen,datos_archivo,boxes)
    
    
    if ruta_carpeta:
        with open(imagen, 'rb') as image_file:
            image_data = image_file.read()
    
        # Crear un objeto Image
        imagen_pil = Image.open(io.BytesIO(image_data))
    
        # Crear un objeto ImageDraw
        dibujo = ImageDraw.Draw(imagen_pil)

  
    
        # Especificar el color del texto en formato RGB (rojo, verde, azul)
        color = (000, 000, 000)  # Negro en este caso
        
    
        for i in range(boxes):
             coordenadas =desempaquetar_coordendas(coordenadas_text_boxes)
             coord_x = coordenadas[i][0]
             coord_y = coordenadas[i][1]
             #posicion = (coord_x, coord_y)
             #dibujo.text(posicion, lista[i], font=ImageFont.truetype(fuente_texto,28), fill=color)
             texto = lista[i]
             lineas = textwrap.wrap(texto, width=18)
             ancho, alto = dibujo.textsize(texto, font=ImageFont.truetype(fuente_texto,28))
             espaciado = 5
             for j, linea in enumerate(lineas):
                 posicion = (coord_x, coord_y + (j * (alto + espaciado)))
                 dibujo.text(posicion, linea, font=ImageFont.truetype(fuente_texto,28), fill=color)

        # Guardar la imagen en la carpeta especificada
        ruta_imagen = os.path.join(ruta_carpeta, f"{nick}_{nombre_meme}.{tipo_img}")
        imagen_pil.save(ruta_imagen, format='PNG')
        
        print(f"Meme guardado exitosamente en: {ruta_carpeta}")
        return imagen_pil
    else:
        print("Ruta de carpeta no encontrada en 'configuracion.json'")

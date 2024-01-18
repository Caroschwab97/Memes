import os


def obtener_coordenadas(imagen, data, boxes):
    """
    Funcion encargada de obtener las coordenadas de cada uno de los cuadros de texto

    Parametros
        - imagen: imagen seleccionada para hacer el meme
        - data: archivo con datos de las imagenes
        - boxes = cantidad  de cuadros de texto del meme

    Retorna
        - Una lista con diccionarios los cuales contienen las coordenadas de cada uno de los
        cuadros de texto.
    """
    datos = data
    img = os.path.basename(imagen)
    coords = []
    for linea in datos:
        if img == linea["image"]:
            for i in range(boxes):
                # print(linea["text_boxes"][i])
                coords.append(linea["text_boxes"][i])
    return coords


def desempaquetar_coordendas(coordenadas):
    """
    Se encarga de separar los valores de las coordenadas, de cada uno de los cuadros de texto.

    Parametros
     - coordenadas: lista de diccionarios, en los cuales se encuentran las coordenadas

    Retorna
        - Lista de listas, donde cada una de las listas contiene las coordenadas correspondientes
        a cada cuadro de texto
    """
    coordenadas_des = []
    for i in range(len(coordenadas)):
        coords = []
        for key, value in coordenadas[i].items():
            coords.append(value)
        coordenadas_des.append(coords)
    return coordenadas_des


def tamaño_contenedor(lista_coords):
    """
    Se encarga de calcular el tamaño del cuadro de texto

    Parametros:
        - lista_coords: lista que contiene las coordenadas de un cuadro de texto

    Retorna
        - Una tupla donde se encuentra el ancho y el alto del cuadro de texto
    """
    # # tamaño total de la caja de texto
    dif_left = lista_coords[2] - lista_coords[0]
    dif_right = lista_coords[3] - lista_coords[1]

    difs = (dif_left, dif_right)
    return difs

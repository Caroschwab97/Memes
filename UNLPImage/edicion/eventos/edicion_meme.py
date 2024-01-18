import PySimpleGUI as sg
import os
import matplotlib.font_manager as fm

from UNLPImage.edicion.acceso_datos.cargar_datos_memes import _guardar_meme, generar_inputs, obtener_cant_boxes
from UNLPImage.logs.log_logica import insertar_log

def edicion(nick, imagen):
    """
    Crea una ventana de generacion de meme, en la cual se le permite
    al usuario seleccionar un tipo de fuente e ingresar el texto que
    desea que contenga el meme.

    Parametros:
    - nick: Nombre del usuario.
    - imagen: El diseño para el meme elegido.
    """
    fuentes = fm.findSystemFonts()
    fuentes_disponibles = [os.path.basename(fuente) for fuente in fuentes]
    
    tipos_img = ["png","jpg"]
    layout = [
        [
         sg.Text("Editar memes", font=("Helvetica", 16)),
         sg.Text(size=(44, 0)),
         sg.Button("< Volver", font=("Helvetica", 12), size=(10, 1), pad=((90, 0), (5, 0))),
        ],
        [sg.Image(filename=imagen, size=(350, 350), key="-MEME-", pad=((8,0),(5,0)))],
        [
         sg.Text("Seleccionar un tipo de fuente", size=(20,1)),
         sg.DropDown(fuentes_disponibles, default_value=fuentes_disponibles[0], key="-FUENTES-"),
        ],
        [
         sg.Text("Agregar texto ", size=(19,1)),
         sg.Column(generar_inputs(imagen))
        ],
        [sg.Text("Nombre del meme", size=(20,1)),
         sg.Input(key=("-NOMBRE-MEME-"), size=(39,1))],
        [
         sg.Text("Seleccionar tipo de imagen:"),
         sg.DropDown(tipos_img, default_value=tipos_img[0], key="-TIPO-IMG-"),
        ],
        [sg.Button("Guardar", size=(10,1))],
    ]

    window = sg.Window("", layout, size=(720, 600), margins=(0, 0))

    textos = []

    while True:
        event, values = window.read()
        match event:
            case sg.WIN_CLOSED:
                window.close()
                break
            case "< Volver":
                window.close()
            case "Guardar":
                for i in range(obtener_cant_boxes(imagen)):
                    texto_ingresado = values[f"-TEXTO{i}-"]
                    if texto_ingresado:
                        textos.append(texto_ingresado)
                nombre_meme_nuevo = values['-NOMBRE-MEME-']
                fuente = values['-FUENTES-']
                tipo_img = values['-TIPO-IMG-']
                if nombre_meme_nuevo != '':
                    _guardar_meme(nick, imagen, textos,fuente,tipo_img,nombre_meme_nuevo)
                    sg.Popup("Meme guardado exitosamente")
                else:
                    nombre_meme_nuevo = 'nombre_meme_default'
                    _guardar_meme(nick, imagen, textos,fuente,tipo_img,nombre_meme_nuevo)
                    sg.Popup("Meme guardado exitosamente")
                nombre_imagen = os.path.basename(imagen)
                palabras = " , ".join(
                    [palabra for texto in textos for palabra in texto.split(",")]
                )
                insertar_log(nick, "nuevo_meme", nombre_imagen, palabras)
                window.close()

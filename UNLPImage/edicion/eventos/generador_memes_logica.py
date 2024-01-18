import PySimpleGUI as sg
import os
from PIL import Image, ImageTk

from UNLPImage.edicion.eventos.edicion_meme import edicion
from UNLPImage.edicion.ventanas.generador_memes import memes_ventana

def generar(nick):

    """
    Genera una ventana de memes y maneja los eventos asociados.

    Parametros:
    - nick: El nombre de usuario.

    """

    window = memes_ventana()

    editar = ''

    while True:
        event, values = window.read()
        match event:
            case sg.WIN_CLOSED:
                window.close()
                break
            case "< Volver":
                window.close()
            case "-EDITAR-":
                window.close()
                if editar != '':
                    edicion(nick, editar)
                else:
                    sg.popup("No ha seleccionado imagen para el meme")
                    ejecutar(nick)
            case _:
               print(event)
               editar = os.path.join('UNLPImage', 'imagenes', 'memes', f'{event}')
               imagen_meme = Image.open(editar)
               imagen_meme.thumbnail((400,400))
               window['-IMG-'].update(data=ImageTk.PhotoImage(imagen_meme))
            

def ejecutar(nick):
    generar(nick)

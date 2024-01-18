import PySimpleGUI as sg
import json
import os
from UNLPImage.edicion.acceso_datos.cargar_datos_memes import _imagenes_memes

def memes_ventana():
    selection_layout = [
        [
            sg.Column(
                _imagenes_memes(), size=(100, 600),scrollable=False, key="-IMGS-"
            )
        ],
    ]

    elements_layout = [
        [sg.Text("Selecciona la plantilla para el meme",font=("Helvetica", 14), pad=((40, 0), (10, 0))),
         sg.Push()
        ],
        [
            sg.Push(),
            sg.Image(key="-IMG-", size=(80,80), enable_events=False),
            sg.Push()    
        ],
        [
            sg.Button(
                "Pasar a edición",
                font=("Helvetica", 12),
                size=(15, 1),
                pad=((35, 0), (15, 0)),
                key='-EDITAR-'
            )
        ],
    ]

    layout = [
        [
            sg.Text("Generar memes", font=("Helvetica", 16)),
            sg.Text(size=(44, 0)),
            sg.Button(
                "< Volver", font=("Helvetica", 12), size=(10, 1), pad=((80, 0), (5, 0))
            ),
        ],
        [sg.Column(selection_layout), sg.Column(elements_layout)],
    ]

    return sg.Window("", layout, size=(720, 600), margins=(0, 0))

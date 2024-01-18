import PySimpleGUI as sg
import os

def crear_ventana(avatares):

    nuevo = os.path.join('UNLPImage', 'imagenes', 'img_sistema',  'nuevo.png')

    # Definir el diseño del formulario con los avatares
    layout = [[sg.Text('UNLPImage',font=('any 15'), justification='left')],
        # Mostrar los avatares en una columna
        [sg.Column(avatares, scrollable=True, key='-AVATARES-', size=(82,200), pad=(240,20))],  
        [sg.Button(image_filename=nuevo, font='any 15', key='+', pad=(245, 0), image_size=(70,70))]
    ]

    # Crear la ventana con el diseño
    return sg.Window('Inicio', layout, size=(600, 415))
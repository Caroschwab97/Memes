import PySimpleGUI as sg
import os

from UNLPImage.perfil.constantes.generos import generos

def ventana_new_perfil():
    layout1 = [
        [sg.Text('Nick o alias', pad=(60, 2, 0, 2))],[sg.InputText(size=(30,2),key="val1", pad=(60, 2, 0, 2))],
        [sg.Text('Nombre', pad=(60, 2, 0, 2))],[sg.InputText(size=(30,2),key="val2", pad=(60, 2, 0, 2))],
        [sg.Text('Edad', pad=(60, 2, 0, 2))],[sg.InputText(size=(30,2),key="val3", pad=(60, 2, 0, 2))],
        [sg.Text('Genero autopercibido', pad=(60, 2, 0, 2))],
        [sg.InputCombo(values=generos, default_value='Seleccione una opcion', size=(28,1),key="val4", pad=(60, 2, 0, 2))],
        [sg.Radio('Otro', "opcion", key="opcion4", pad=(60,2,0,2))],[sg.InputText(size=(30,2),key="val5", pad=(60, 2, 0,              2))]
     ]

    # Construye la ruta de archivo utilizando os.path.join()
    ruta = os.path.join('UNLPImage', 'imagenes', 'img_sistema', 'sin_imagen.png')

    layout2 = [
               [sg.InputText(key='file_path', size=(20,1), enable_events=True),
                sg.FileBrowse('Buscar', file_types=(('Imágenes', '*.png*'),))],
               [sg.Image(filename=ruta, key='-AVATAR-', size=(100,100), pad=(40, 20, 0, 0))],
               [sg.Button('Seleccionar Avatar', pad=(30, 0, 0, 0))]
    ]

    layout = [[sg.Text('Nuevo Perfil',font=('Helvetica', 16)),sg.Text(size=(44,0)),
               sg.Button('⬅ Volver',font=('Helvetica',12),size=(10,1),pad=(0, 0, 0, 0))],
              [sg.Text(size=(0,0))],
              [sg.Column(layout1), sg.Column(layout2)],
              [sg.Button('Guardar', key='-GUARDAR-',font=('Helvetica',12),size=(20,1),pad=((10, 0), (50, 0)))]
    ]

    return sg.Window('Nuevo perfil', layout, size=(600,415),margins=(0,0))
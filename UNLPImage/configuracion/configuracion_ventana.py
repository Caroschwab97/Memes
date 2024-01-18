import PySimpleGUI as sg

from UNLPImage.configuracion.configuracion_acceso_datos import cargar_configuracion

def config():
    dirs = cargar_configuracion()

    layout = [
        [sg.Text('Configuracion',font=('Helvetica', 16)),sg.Text(size=(42,1)),
         sg.Button('< Volver',font=('Helvetica', 12),size=(10,1), pad=(2, 0))],
        [sg.Text('Repositorio de imagenes', pad=((100, 0),(35,0)))],
        [sg.Text(size=(10,2)), sg.InputText(dirs['imagenes'], size=(25,4), key="val1", pad=(2,0)),
         sg.FolderBrowse('Seleccionar', size=(24,2),pad=(2,2))],
        [sg.Text('Directorio de collages', pad=(100, 0))],
        [sg.Text(size=(10,2)), sg.InputText(dirs['collages'], size=(25,4), key="val2", pad=(2,0)),
         sg.FolderBrowse('Seleccionar', size=(24,2),pad=(2,2))],
        [sg.Text('Directorio de memes', pad=(100, 0))],
        [sg.Text(size=(10,2)), sg.InputText(dirs['memes'], size=(25,4), key="val3", pad=(2,0)),
         sg.FolderBrowse('Seleccionar', size=(24,2),pad=(2,2))],
        [sg.Button('Guardar', font=('Helvetica',12), size=(20,1), pad=((8, 0), (90,0)))]
    ]

    return sg.Window('Configuracion', layout, size=(600,415),margins=(0,0))
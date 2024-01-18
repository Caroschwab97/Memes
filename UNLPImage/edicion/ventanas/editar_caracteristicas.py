import PySimpleGUI as sg

def ventana():
    # Definimos el layout de la ventana principal
    layout = [
        [sg.Text('Imagen seleccionada:'),
         sg.Button('< Volver',font=('Helvetica',12),size=(10,1), pad=((455,0),(0,10)))],
        [sg.Input(key='file', visible=True), sg.FileBrowse('Seleccionar imagen')],
        [sg.Button('Ver metadatos', size=(15,1))],
        [sg.Text('Editar metadatos')],
        [sg.Text('Fecha de creación: ', size=(15,1)), sg.Input(key='fecha', size=(40,1))],
        [sg.Text('Tamaño del archivo:', size=(15,1)), sg.Input(key='size', size=(40,1))],
        [sg.Text('Formato de imagen: ', size=(15,1)), sg.Input(key='formato', size=(40,1))],
        [sg.Button('Guardar', size=(15,1))],
        [sg.Text('Tags de la imagen:')],
        [sg.Listbox(values=[], size=(30, 5), key='tag list')],
        [sg.Text('Agregar tag:', size=(10,1)), sg.Input(key='tag nueva'), sg.Button('Agregar', size=(10,1))],
        [sg.Text('Eliminar tag:', size=(10,1)), sg.Input(key='eliminar tag'), sg.Button('Eliminar', size=(10,1))]
    ]

    return sg.Window('Editor de caracteristicas de imagenes', layout, size=(720,480))

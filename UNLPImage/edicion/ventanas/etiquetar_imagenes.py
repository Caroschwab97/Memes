import PySimpleGUI as sg

def ventana():
    layout1 = [
               [sg.Text('Seleccione una imagen', pad=(20, 0, 0, 0))],
               [sg.InputText(key='file', enable_events=True, size=(35,2), pad=(20, 0, 0, 0)), sg.FileBrowse('Buscar')],
               [sg.Button('Seleccionar imagen', pad=(20, 0, 0, 0))],
               [sg.Text('tag', pad=(20, 2, 0, 2))],
               [sg.InputText(size=(35,2),key="val1", pad=(20, 2, 0, 2)),sg.Button('agregar', key='agregar ')],
               [sg.Text('texto descriptivo', pad=(20, 2, 0, 2))],
               [sg.InputText(size=(35,2),key="val2", pad=(20, 2, 0, 2)),sg.Button('agregar', key='agregar')]
              ]

    layout2 = [ 
               [sg.Text(size=(8,2)),sg.Text('imagen seleccionada', key='img_select')],
               [sg.Image(key='imagen', size=(150,150), pad=(80, 10, 0, 0))],
               [sg.Text('', key='datos_imagen', pad=(30, 10, 0, 0))],
               [sg.Text('', key='lista_tags',background_color= None)],
               [sg.Text('',key='descripcion')]
              ]

    layout = [
              [sg.Text('Etiquetar imagenes',font=('Helvetica', 16), pad=((0,0),(0,10))),
               sg.Text(size=(50,0)),sg.Button('< Volver',font=('Helvetica',12),size=(10,1))],
              [sg.Column(layout1), sg.Column(layout2)],
              [sg.Button('edicion de caracteristicas',font=('Helvetica',12),size=(20,1),pad=((10, 0), (60, 0))),
               sg.Button('guardar',font=('Helvetica',12),size=(20,1),pad=((310, 0), (60, 0)))]
             ]

    return sg.Window('Visualizador de imágenes', layout, size=(720,480))
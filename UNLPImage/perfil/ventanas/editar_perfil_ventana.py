import PySimpleGUI as sg

from UNLPImage.perfil.constantes.generos import generos
from UNLPImage.perfil.acceso_datos.perfil_datos import buscar_perfil

def ventana_perfil(nick):   

    perfil = buscar_perfil(nick)            
     
    #lee la imagen del avatar actual
    with open(perfil['avatar'], 'rb') as image_file:
        image_data = image_file.read()
    
    layout = [
       [sg.Text('Editar Perfil',font=('Helvetica', 16)),sg.Text(size=(44,1)),
        sg.Button('⬅ Volver',font=('Helvetica', 12),size=(10,1), pad=(2, 0))],
       [sg.Text('Nick:', font=('Helvetica', 12), pad=((45,0),(15,5))),
        sg.Text(nick, font=('Helvetica', 12, 'bold'), pad=((105,0),(15,5)))],
       [sg.Text('     Nombre:',size=(15, 1), font=('Helvetica',12),pad=(25,5)), sg.InputText(perfil['nombre'],                 key='nombre', pad=(0,5))],
       [sg.Text('     Edad:', size=(15, 1), font=('Helvetica',12),pad=(25,5)), sg.InputText(perfil['edad'], key='edad',
        pad=(0,5))],
       [sg.Text('     Genero:', size=(15, 1), font=('Helvetica',12),pad=(25,5)), sg.InputCombo(values=generos,                       default_value=perfil['genero'], size=(43,1), key='genero', pad=(0,5))],
       [sg.Text('     Avatar:', size=(15, 1), font=('Helvetica',12),pad=(25,5)), sg.Image(data=image_data,                         key='imagen', size=(125,125), pad=(0, 5))],
       [sg.Text(size=(2,0)), sg.InputText(key='file', enable_events=True, size=(28,2), pad=(20, 2, 0, 2)), 
        sg.FileBrowse('Buscar', size=(12,1), file_types=(('Imágenes', '*.png*'),)),
        sg.Button('Seleccionar',font=('Helvetica',11),size=(12,1),pad=(15,0))],
       [sg.Text(size=(0,0))],
       [sg.Button('Guardar cambios',font=('Helvetica',12),size=(15,1),pad=(8,0)),
        sg.Button('Eliminar',font=('Helvetica',12),size=(15,1),pad=(8,0))]
    ]


    return sg.Window('Perfil', layout, size=(600,415),margins=(0,0))
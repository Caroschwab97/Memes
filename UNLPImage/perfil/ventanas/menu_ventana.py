import PySimpleGUI as sg

from UNLPImage.perfil.acceso_datos.perfil_datos import buscar_perfil

def obtener_avatar_actual(nick):
     perfil = buscar_perfil(nick)           
     return perfil['avatar']

def main(nick):
    
    layout = [
        [sg.Button(image_filename=obtener_avatar_actual(nick),image_size=(45,45),key="-EDITAR-", pad=(10,2)),
         sg.Text(size=(48,2)),
         sg.Button("⚙",font=('Helvetica',10),size=(4,2), border_width=3,button_color=('white','DodgerBlue4')),
         sg.Button('❔',font=('Helvetica',10),size=(4,2), border_width=3,button_color=('white','DodgerBlue4'))],
        [sg.Text(f" {nick}",font=('Arial', 12, 'bold'),size=(10,1),key="-EDITAR-",text_color='white')],
        [sg.Button('Etiquetar imagenes',
                   font=('Helvetica', 10, 'bold'),
                   size=(25,2),
                   pad=((180,0), (10,4)),
                   border_width=4)],
        [sg.Button('Generar memes',
                   font=('Helvetica', 10, 'bold'),
                   size=(25,2),
                   pad=(180,4),
                   border_width=4)],
        [sg.Button('Generar collage',
                   font=('Helvetica', 10, 'bold'),
                   size=(25,2),
                   pad=(180,4),
                   border_width=4)],
        [sg.Button('Ver Graficos',
                   font=('Helvetica', 10, 'bold'),
                   size=(25,2),
                   pad=(180,3),
                   border_width=4)],
        [sg.Button('Salir',
                   font=('Helvetica', 10, 'bold'),
                   size=(25,2),
                   pad=(180,3),
                   border_width=4)]

    ]

    return sg.Window('Menu', layout, size=(600,460))

    
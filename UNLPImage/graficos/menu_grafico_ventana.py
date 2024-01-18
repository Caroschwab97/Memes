import PySimpleGUI as sg

from UNLPImage.graficos.mostrar_grafico_dispersion import grafico_dispersion
from UNLPImage.graficos.mostrar_grafico_nube import grafico_nube
from UNLPImage.graficos.mostrar_grafico_vertical import grafico_barra_vertical
from UNLPImage.graficos.mostrar_grafico_torta import grafico_torta
from UNLPImage.graficos.mostrar_grafico_bytes_promedio import grafico_barras_bytes

def grafico_ventana():

    layout = [
        [sg.Button('Volver',font=('Helvetica',10),size=(8,2), border_width=3,button_color=('white','DodgerBlue4'))],
        [sg.Button('Usos Por Dia',
                   font=('Helvetica', 10, 'bold'),
                   size=(25,2),
                   pad=((180,0), (10,4)),
                   border_width=4)],
        [sg.Button('Nube De Palabras',
                   font=('Helvetica', 10, 'bold'),
                   size=(25,2),
                   pad=(180,4),
                   border_width=4)],
        [sg.Button('Uso Por Operacion',
                   font=('Helvetica', 10, 'bold'),
                   size=(25,2),
                   pad=(180,4),
                   border_width=4)],
        [sg.Button('Dispersion Alto_ancho',
                   font=('Helvetica', 10, 'bold'),
                   size=(25,2),
                   pad=(180,4),
                   border_width=4)],
        [sg.Button('Promedio de bytes',
                   font=('Helvetica', 10, 'bold'),
                   size=(25,2),
                   pad=(180,4),
                   border_width=4)]

    ]

    # Crear la ventana de PySimpleGUI
    window = sg.Window('Menu de Graficos', layout, size=(600,460))


    # Bucle principal de eventos de PySimpleGUI
    while True:
        event, values = window.read() 

        match event:
            case sg.WIN_CLOSED:
                window.close()
                break
            case 'Usos Por Dia':
                window.hide()
                grafico_barra_vertical()
                window.un_hide()
            case 'Uso Por Operacion':
                window.hide()
                grafico_torta()
                window.un_hide()
            case 'Nube De Palabras':
                window.hide()
                grafico_nube()
                window.un_hide()
            case 'Dispersion Alto_ancho':
                window.hide()
                grafico_dispersion()
                window.un_hide()
            case 'Promedio de bytes':
                window.hide()
                grafico_barras_bytes()
                window.un_hide()
            case 'Volver':
                window.close()
            

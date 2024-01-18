import PySimpleGUI as sg

from UNLPImage.perfil.acceso_datos.avatares_inicio import avatares
from UNLPImage.perfil.eventos.menu_logica import mostrar_menu
from UNLPImage.perfil.eventos.nuevo_perfil_logica import new_perfil
from UNLPImage.perfil.ventanas.inicio_ventana import crear_ventana

def mostrar_perfiles():

    """
    Abre una ventana para mostrar los perfiles de usuario y permite crear un nuevo perfil.

    Devuelve:
        Ninguno
    """
    
    ventana = crear_ventana(avatares())

    while True:
        event, values = ventana.read()

        if event == sg.WIN_CLOSED:
            ventana.close()
            break
        elif event != '+':
            ventana.close()
            mostrar_menu(event)
            go()
        elif event == '+':
            ventana.close()        
            new_perfil()
            go()


def go():
    mostrar_perfiles()
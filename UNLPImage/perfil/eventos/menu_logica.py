import PySimpleGUI as sg

from UNLPImage.configuracion.configuracion_logica import setting

from UNLPImage.edicion.eventos.generador_memes_logica import ejecutar
from UNLPImage.edicion.eventos.generador_collages_logica import crear
from UNLPImage.edicion.eventos.etiquetar_imagen_logica import etiquetar

from UNLPImage.graficos.menu_grafico_ventana import grafico_ventana

from UNLPImage.perfil.acceso_datos.validador_nick import validar_nick
from UNLPImage.perfil.eventos.editar_perfil_logica import editar_perfil
from UNLPImage.perfil.ventanas.menu_ventana import main


def mostrar_popup():
    mensaje = '''Bienvenido al programa 'UNLPImage'.

    Puedes realizar las siguientes acciones:

    1. Generar memes: Esta función te permite crear memes personalizados a partir de imágenes y texto.

    2. Generar collages: Con esta funcionalidad, puedes combinar varias imágenes en un collage creativo.

    3. Etiquetar imágenes: Esta opción te permite añadir etiquetas o información adicional a tus imágenes.

    4. Modificar datos de perfil: Aquí puedes actualizar y gestionar la información de tu perfil de usuario.

    5. Configuración del programa: En esta sección, puedes personalizar la configuración del programa según tus preferencias.

       Esperamos que disfrutes usando nuestro programa. ¡Diviértete!

    - El equipo de desarrollo'''

    sg.popup('Información del programa', mensaje)    


def loop(nick):

    """
    Inicia el bucle del menu de la aplicación UNLPImage, mostrando la ventana  y manejando los eventos.

    Args:
        nick (str): El nombre de usuario asociado a la sesión.

    """

    window = main(nick)

    while True:
        event, values = window.read()
  
        match event:
            case sg.WIN_CLOSED:
                window.close()
                break
            case 'Salir':
                window.close()  
            case '⚙':
                window.hide()
                setting(nick)
                window.un_hide()
            case '❔':
                mostrar_popup()
            case '-EDITAR-':
                window.close()
                editar_perfil(nick)
                try:
                    validar_nick(nick)
                except ValueError:
                    mostrar_menu(nick)
            case 'Generar memes':
                window.close()
                ejecutar(nick)
                mostrar_menu(nick)
            case 'Generar collage':
                window.close()
                crear(nick)
                mostrar_menu(nick)
            case 'Etiquetar imagenes':
                window.hide()
                etiquetar(nick)
                window.un_hide()
            case 'Ver Graficos':
                window.hide()
                grafico_ventana()
                window.un_hide()


def mostrar_menu(nick):
    loop(nick)
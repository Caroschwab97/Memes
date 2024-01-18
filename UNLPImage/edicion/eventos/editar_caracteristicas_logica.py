import PySimpleGUI as sg
from datetime import date
from PIL import Image

from UNLPImage.edicion.acceso_datos.modificar_tamaño import actualizar_tamanio
from UNLPImage.edicion.acceso_datos.dar_baja_tag import eliminar_tag
from UNLPImage.edicion.acceso_datos.dar_alta_tag import agregar_tag
from UNLPImage.edicion.acceso_datos.listar_tag_actuales import recuperar_tags
from UNLPImage.edicion.acceso_datos.metadatos_imagen import obtener_metadatos_imagen
from UNLPImage.edicion.ventanas.editar_caracteristicas import ventana

from UNLPImage.logs.log_logica import insertar_log


def mostrar_metadatos(window,datos):

    """
    Actualiza los elementos de una ventana con los metadatos proporcionados.
    Args:
        window (objeto): Objeto de la ventana que contiene los elementos a actualizar.
        datos (dict): Diccionario que contiene los metadatos a mostrar.
    """

    window['fecha'].update(datos['fecha_actualizacion'])
    window['size'].update(datos['size'])
    window['formato'].update(datos['tipo'])


def editar(nick):

    """
     Abre una ventana para editar las características de la imagen.
     Args:
         nick (str): El nick del usuario.
     Returns:
        None
    """
    
    window = ventana()

    while True: 
        event, values = window.read()

        match event:
            case sg.WIN_CLOSED: 
                window.close()              
                break
            case '< Volver':
                window.close()
            case 'Ver metadatos':
                if values['file']:
                    datos = obtener_metadatos_imagen(values['file'],nick)
                    mostrar_metadatos(window,datos)
                    lista_tags = recuperar_tags(values['file'])
                    window['tag list'].update(lista_tags)
                else:
                    sg.popup("No selecciono ninguna imagen")
            case 'Agregar':
                if values['tag nueva']:
                    if values['file']:
                        agregar_tag(values['file'],values['tag nueva'],nick)
                        lista_tags = recuperar_tags(values['file'])
                        window['tag list'].update(lista_tags)
                        window['tag nueva'].update('')
                        insertar_log(nick, "modifico imagen previamente clasificada")
                    else:
                        sg.popup('no selecciono ninguna imagen')
                else:
                    sg.popup('no ingreso ningun tag')
            case 'Eliminar':
                if values['eliminar tag']:
                    if values['file']:
                        eliminar_tag(values['file'], values['eliminar tag'],nick)
                        window['eliminar tag'].update('')
                        lista_tags = recuperar_tags(values['file'])
                        window['tag list'].update(lista_tags)
                        insertar_log(nick, "modifico imagen previamente clasificada")
                    else:
                        sg.popup('no selecciono ninguna imagen')
                else:
                    sg.popup('no ingreso ningun tag')
            case 'Guardar':
                if values['file']:
                    if values['size']:
                        actualizar_tamanio(values['file'],values['size'],nick)
                        window['file'].update('')
                        insertar_log(nick, "modifico imagen previamente clasificada")
                else:
                    sg.popup('no selecciono ninguna imagen')
                    

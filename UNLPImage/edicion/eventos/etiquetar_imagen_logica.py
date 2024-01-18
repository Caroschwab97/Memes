import base64
import os
import PySimpleGUI as sg
import re
from datetime import date
from PIL import Image

from UNLPImage.edicion.acceso_datos.metadatos_imagen import obtener_metadatos_imagen
from UNLPImage.edicion.acceso_datos.cargar_archivo_csv import crear_archivo_csv
from UNLPImage.edicion.eventos.editar_caracteristicas_logica import editar
from UNLPImage.edicion.acceso_datos.listar_tag_actuales import recuperar_tags
from UNLPImage.edicion.ventanas.etiquetar_imagenes import ventana
from UNLPImage.logs.log_logica import insertar_log


def leo_imagen(imagen):

    """
     Hace el pasaje de la imagen a imagen en base64
     Args:
         imagen (str): La ruta de la imagen
     Returns:
        (str) la imagen en base64
    """

    with open(imagen, 'rb') as image_file:
        image_data = image_file.read()
        # Convertir la imagen a Base64
        image_base64 = base64.b64encode(image_data).decode('utf-8')
    return image_base64


def etiquetar(nick):

    """
     Abre una ventana para guardar las características de la imagen y agregar tags y descripcion
     Args:
         nick (str): El nick del usuario.
     Returns:
        None
    """


    listaTags=[]
    textoDescriptivo = ''
    texto_tags='tags: '

    window = ventana()

    while True:
        event, values = window.read()

        match event:
            case sg.WIN_CLOSED: 
                window.close()              
                break
            case '< Volver':
                window.close()
            case 'Seleccionar imagen':
                listaTags=[]
                window['lista_tags'].update('')
                window['lista_tags'].update(background_color= None) 
                filename = values['file']
                if filename:
                    imagen = Image.open(filename)
                    img_base64 = leo_imagen(filename)
                    # Actualizamos el elemento de la ventana correspondiente a la imagen
                    window['imagen'].update(data=img_base64,size=(150,150))
                    window['img_select'].update(os.path.basename(filename))
                    resolucion = re.sub(r'\((\d+), (\d+)\)', r'\1, \2', str(imagen.size))
                    window['datos_imagen'].update('| ' + str(f"imagen.{imagen.format}")+ '  | '
                                                        + str(resolucion) + ' px  | '
                           + str(f"{round(os.path.getsize(filename) / (1024 * 1024), 2)} MB") + ' |')
                    lista = recuperar_tags(filename)
                    if (lista):
                        texto_tags ="tags: "+" ".join(str(elem) for elem in lista)
                        window['lista_tags'].update(texto_tags)
                        window['lista_tags'].update(background_color= 'grey') 
                else:
                    sg.popup('no ingreso ninguna imagen')
            case 'agregar ':
                t=values['val1']
                if t:
                    listaTags.append(t)
                    window['val1'].update('')
                    texto_tags += (" "+ t)
                    window['lista_tags'].update(texto_tags)         
                else: 
                    sg.popup('no ingreso ningun tag')
            case 'agregar':
                textoDescriptivo = values['val2']
                window['val2'].update('')  
                window['descripcion'].update('descripcion: ' + textoDescriptivo)
            case 'guardar':
                if not(recuperar_tags(values['file'])):
                    if values['file']:
                        datos=obtener_metadatos_imagen(values['file'],nick)
                        crear_archivo_csv(datos,listaTags,textoDescriptivo)
                        insertar_log(nick, "nueva imagen clasificada")
                        window['file'].update('')
                    else:
                        sg.popup('no selecciono ninguna imagen')
                else:
                        sg.popup_error( 'no se puede guardar una foto que ya esta guardada con anterioridad, vaya a edicion de caracteristicas', title='Error')
            case 'edicion de caracteristicas':
                window.hide()
                editar(nick)
                window.un_hide()
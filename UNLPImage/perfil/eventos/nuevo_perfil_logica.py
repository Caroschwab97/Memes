import PySimpleGUI as sg
import os

from UNLPImage.logs.log_logica import insertar_log
from UNLPImage.perfil.acceso_datos.nuevo_perfil_datos import guardar_perfil, guardo_imagen
from UNLPImage.perfil.acceso_datos.validador_nick import validar_nick
from UNLPImage.perfil.validadores.validador_edad import verificar_edad
from UNLPImage.perfil.ventanas.nuevo_perfil_ventana import ventana_new_perfil

    
def new_perfil():

    """
    Muestra una ventana para crear un nuevo perfil de usuario y realizar validaciones en los datos ingresados.

    Returns:
        None
    """

    window = ventana_new_perfil()

    while True:
        event, values = window.read()

        match event:
            case sg.WIN_CLOSED:
                window.close()
                break
            case '-GUARDAR-':
                try:
                    validar_nick(values['val1'])
                    verificar_edad(values['val3'])
                    img=''
                    if values['file_path']:
                        img = guardo_imagen(values['file_path'], values['val1'])
                    else:
                        raise ValueError('No ha seleccionado imagen de perfil')
                    if values['val5']:
                        datos = [values['val1'], values['val2'], values['val3'], values['val5'], img]
                    else:
                        datos = [values['val1'], values['val2'], values['val3'], values['val4'], img]
                    guardar_perfil(datos)
                except ValueError as e:
                    # Mostrar el error en un popup
                    sg.popup_error(str(e), title='Error')
                else:
                    # Sino se genera una excepcion, cierra la ventana y vuelve a la ventana de inicio
                    # con el nuevo perfil agregado
                    insertar_log(values['val1'], "creacion de nuevo perfil")
                    window.close()
            case 'Seleccionar Avatar':
                file_path = values['file_path']
                if file_path:   
                    # Actualizar la ventana con la imagen cargada
                    window['-AVATAR-'].update(filename=file_path,size=(100,100))
            case '⬅ Volver':
                window.close()
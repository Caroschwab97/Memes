import PySimpleGUI as sg

from UNLPImage.logs.log_logica import insertar_log
from UNLPImage.perfil.acceso_datos.editar_perfil_datos import guardar_datos
from UNLPImage.perfil.acceso_datos.eliminar_perfil import baja_perfil
from UNLPImage.perfil.acceso_datos.nuevo_perfil_datos import guardo_imagen
from UNLPImage.perfil.acceso_datos.perfil_datos import buscar_perfil
from UNLPImage.perfil.validadores.validador_edad import verificar_edad
from UNLPImage.perfil.ventanas.editar_perfil_ventana import ventana_perfil


def editar_perfil(nick):

    """
    Muestra una ventana para editar un perfil de usuario, permitiendo cambiar el nombre, la edad,
    el genero y la imagen de perfil.

    Args:
        nick (str): Nombre de usuario del perfil a editar.

    Returns:
        None
    """

    window = ventana_perfil(nick)

    while True:
        event, values = window.read()

        match event:
            case sg.WIN_CLOSED: 
                window.close()             
                break
            case '⬅ Volver':
                window.close()
            case 'Seleccionar':
                if values['file']:
                    window['imagen'].update(values['file'],size=(125,125))
            case 'Guardar cambios':
                try:
                    verificar_edad(values['edad'])
                    image = '#'
                    if values['file']:
                        image = guardo_imagen(values['file'],nick)
                    else:
                        perfil = buscar_perfil(nick)
                        image = perfil['avatar']
                    datos = [values['nombre'],values['edad'],values['genero'],image]
                    # Guarda los datos actualizados y cierra la GUI
                    guardar_datos(datos,nick)
                except ValueError as e:
                    # Mostrar el error en un popup
                    sg.popup_error(str(e), title='Error')
                else:
                    insertar_log(nick, "modificacion de perfil")
                    window.close()
            case 'Eliminar':
                mensaje_confirmacion = f"¿Deseas eliminar el perfil '{nick}'?"
                confirmado = sg.popup_yes_no("Confirmación", mensaje_confirmacion)
                if confirmado == "Yes":
                    if baja_perfil(nick):
                        sg.popup("Perfil eliminado", f"El perfil '{nick}' ha sido eliminado correctamente.")
                        window.close()
                else:
                    sg.popup("Eliminación cancelada", "La eliminación del perfil ha sido cancelada.")
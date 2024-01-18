import PySimpleGUI as sg

from UNLPImage.configuracion.configuracion_ventana import config
from UNLPImage.configuracion.configuracion_acceso_datos import actualizar_configuracion
from UNLPImage.logs.log_logica import insertar_log 

def configurar (nick):

    """
    Configura los directorios para el usuario identificado por 'nick'.

    Argumentos:
    - nick (str): Nombre de usuario.

    Comportamiento:
    - Muestra una ventana de configuracion.
    - Permite al usuario seleccionar directorios para diferentes categorias.
    - Guarda la configuracion en un diccionario llamado 'directorios'.
    - Actualiza la configuracion en algun lugar.
    - Cierra la ventana de configuracion y vuelve a la funcion 'loop(nick)'.

    """
    
    directorios = {
                   "imagenes": None,
                   "collages": None,
                   "memes": None
                  }

    window = config()

    while True:
        event, values = window.read()
        
        match event:
            case sg.WIN_CLOSED: 
                window.close()              
                break
            case '< Volver':
                window.close()
            case 'Guardar':
                # Hacer algo con las carpetas seleccionadas
                if values["val1"]:
                    directorios['imagenes'] = values["val1"]
                    #print(values["val1"])
                if values["val2"]:
                    directorios['collages'] = values["val2"]
                if values["val3"]:
                    directorios['memes'] = values["val3"]
                insertar_log(nick, "Cambio Configuracion")
                actualizar_configuracion(directorios)
                window.close()

    
def setting(nick):
    directorios = configurar(nick)
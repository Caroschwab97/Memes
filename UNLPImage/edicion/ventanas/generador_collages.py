import PySimpleGUI as sg
import PIL

from UNLPImage.edicion.eventos.generador_collages_logica import _plantillas, _imagenes, crear_collage, traer_selectores, traer_datos_plantilla_json

def ventana_collage():

    plantillas = _plantillas()

    cant_plant = len(plantillas)
    mitad_1 = cant_plant/2

    layout = [
              [sg.Text('Generador de Collage',font=('Helvetica', 24)),
               sg.Push(),
               sg.Button('< Volver',font=('Helvetica', 12), size=(10,1), pad=((0,10),(5,0)))],
              [sg.Push(),
               sg.Text('Elegí la plantilla para el collage',font=('Helvetica', 18)),
               sg.Push()
              ],
              [sg.Push(),
               sg.Column(plantillas[0:int(mitad_1)], size= (200, 400), scrollable=False), 
               sg.Column(plantillas[int(mitad_1):cant_plant], size= (200, 400), scrollable=False),
               sg.Push()],
             ]

    return sg.Window('', layout, size=(800,600),margins=(0,0))

def ventana_collage_2(plantilla_ingresada):
    
    imagenes = _imagenes()
    
    nuevo_collage = crear_collage(plantilla_ingresada)
    
    seleccionadores_ubicacion = traer_selectores(nuevo_collage)


    layout = [
              [sg.Text('Generador de Collage',font=('Helvetica', 24)),
               sg.Push(),
               sg.Button('❔',font=('Helvetica',10),size=(4,2), border_width=3,button_color=('white','DodgerBlue4'))
               ],
              [
               sg.Text('Elegí las imagenes para el collage',font=('Helvetica', 18)),
               sg.Push()
              ],
              [  
                sg.Text('Elegí el título para el collage',font=('Helvetica', 14)),
                sg.Input('', enable_events=True, key='-INPUT-', font=('Helvetica', 16), justification='left')
              ],
              [
               sg.Column(imagenes, scrollable=True), 
               sg.Push(), 
               sg.Column(seleccionadores_ubicacion, scrollable=False),
               sg.Push(), 
               sg.Image(key="-IMAGEN-"), 
               sg.Push()
               ],
              [ 
               sg.Button('< Volver',font=('Helvetica', 12), size=(10,1), pad=((0,10),(5,0))), 
               sg.Push(),
               sg.Button('Actualizar',font=('Helvetica', 15), size=(15,1), pad=((0,10),(5,0))), 
               sg.Push(),
               sg.Button('Guardar',font=('Helvetica', 12), size=(10,1), pad=((0,10),(5,0)))]
             ]

    return sg.Window('', layout, size=(900, 600),margins=(0,0), finalize=True)
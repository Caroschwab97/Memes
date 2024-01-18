import json
import os
import PySimpleGUI as sg

from UNLPImage.edicion.acceso_datos.listar_tag_actuales import recuperar_tags
from UNLPImage.logs.log_logica import insertar_log
from PIL import Image as Pil_image, ImageTk as Pil_imageTk, ImageOps as Pil_imageOps, ImageDraw as Pil_imageDraw


from UNLPImage.edicion.clases.collage import Collage
    
####################### FUNCIONES PARA CREAR VENTANAS #######################
def crear(nick):

    """
    Crea la ventana 1 de generacion de collages y maneja los eventos asociados. Esta ventana es la que muestra las plantillas disponibles para su elección

    Parametros:
    - nick: El nombre de usuario.

    """

    from UNLPImage.edicion.ventanas.generador_collages import ventana_collage

    window = ventana_collage()

    while True:
        event, values = window.read()

        match event:
            case sg.WIN_CLOSED: 
                window.close()              
                break
            case '< Volver':
                window.close()
                break
            case _:
                window.close()
                enviar_plantilla(nick, event)
                break
  
def enviar_plantilla(nick, plantilla):

    """
    Crea la ventana 2 de generacion de collages y maneja los eventos asociados. 
    Aquí es donde se genera el collage en tiempo real con el manejo de imágenes, su ubicación en el espacio del collage y la asignación de su titulo, para poder guardarlo.

    Parametros:
    - nick: El nombre de usuario.
    - plantilla: El diseño de plantilla elegido

    """

    from UNLPImage.edicion.ventanas.generador_collages import ventana_collage_2

    window = ventana_collage_2(plantilla)

    ## Configuro el area donde se va a armar el collage
    imagen_original = Pil_image.new('RGB', (400, 400))
    imagen_convertida = Pil_imageTk.PhotoImage(imagen_original)
    window['-IMAGEN-'].update(data=imagen_convertida)

    nombre_imagen_seleccionada = "NO_DATA_SELECCIONADA"

    nuevo_collage = crear_collage(plantilla)
    titulo_collage = "NO_DATA_SELECCIONADA"

    while True:
        event, values = window.read()

        match event:
            case sg.WIN_CLOSED: 
                window.close()  
                break    
            case '❔':
                mostrar_popup_funcionalidades()
            case '< Volver':
                window.close()
                crear(nick)
            case '-INPUT-':
                titulo_collage = values['-INPUT-']
            case 'Guardar':
                ##window.close()
                resp = confirmar_nombre_collage(nuevo_collage.generar_filename())
                if (resp):
                    try:
                        imagen_original.save(f'UNLPImage/imagenes/collages_guardados/{nuevo_collage.generar_filename()}.png')   
                        enviar_informacion_al_csv(nick, nuevo_collage)
                        sg.popup_ok(f"Tu collage '{nuevo_collage.titulo}' se guardó correctamente")
                    except Exception:
                        e = "Error al guardar el Collage, intente nuevamente más tarde"
                        print(e)
                        sg.popup_ok(e)            
            case 'Actualizar':
                ##print(values)

                zona = extraer_zona(values) or "NULL"
                if (zona != "NULL"):
                    ##print(zona)
                    nuevo_collage.sumar_imagen_en_posicion(zona, nombre_imagen_seleccionada)
                    ##print(nuevo_collage.imprimir_lugares())
                

                    actualizar_vista_previa(imagen_original, nuevo_collage.lugares, zona)    
                else:
                    sg.popup_ok("Ingrese una zona para agregar la imagen")
                
                nuevo_collage.definir_titulo(titulo_collage)
                actualizar_titulo(imagen_original, nuevo_collage.titulo)

                imagen_convertida = Pil_imageTk.PhotoImage(imagen_original)
                window['-IMAGEN-'].update(data=imagen_convertida)
            ## Esto lo hago asumiendo que todo otro evento que no sea los que estan arriba, son selecciones de imagenes
            case _:
                ##print(event)
                nombre_imagen_seleccionada = event

####################### FUNCIONES PARA CREAR COLLAGE #######################

def crear_collage(nombre_plantilla):

    """
    Funcion que crea una instancia de la clase Collage en base a la plantilla ingresada por parámetro

    Parametros:
    - nombre_plantilla: El nombre del archivo de la plantilla correspondiente.

    Devuelve:
    - Instancia de objeto Collage con la información propia de la plantilla elegida

    """

    plantilla = traer_datos_plantilla_json(nombre_plantilla)
    return Collage(plantilla['espacios'], plantilla['lugares'], plantilla['ruta'])

def traer_datos_plantilla_json(nombre_plantilla, clave='nombre'):

    """
    Trae los datos de una plantilla desde el JSON que contiene la información.

    Parametros:
    - nombre_plantilla: El nombre del archivo de la plantilla correspondiente.
    - clave: El nombre de la clave con el que se compara

    Devuelve
    - Diccionario con datos de la plantilla encontrada, basada en la estructura del JSON de Plantillas

    """

    ruta_archivo = os.path.join('UNLPImage', 'archivos', 'plantillas.json')
    try:
    ##Agregar excepcion
        with open(ruta_archivo, "r") as archivo:
            plantillas_json = json.load(archivo)
            for pl in plantillas_json:
                if (pl[clave] == nombre_plantilla):
                    return pl
    except FileNotFoundError:
        print('Archivo no encontrado')
        return False

####################### FUNCIONES PARA CREAR SELECTORES #######################

"""
    Crea los elementos "Radio" basandose en la información del Collage enviado mediante parámetro.

    Parametros:
    - plantilla: Instancia de la clase Collage.

    Devuelve
    - Lista con los elementos "Radio" creados, con los valores de Nombre y Key, puestos en base a la información de la Clase collage enviada por parámetro. 

    """

def traer_selectores (plantilla):
    try:
        seleccionadores_imagenes = []
        for keyDict, value in plantilla.lugares.items():
            campo = [sg.Radio(f"{value['nombre']}", key=f"-ZONA_{keyDict}-", group_id=1)]
            seleccionadores_imagenes.append(campo)
        return seleccionadores_imagenes
    except Exception:
        print("Error en la plantilla elegida")

####################### FUNCIONES PARA ACTUALIZAR COLLAGE #######################

"""
    Actualiza el estado del elemento Image de PIL con la información traida mediante parámetro.

    Parametros:
    - collage: Elemento tipo Image de PILLOW.
    - diccionario_para_collage: Diccionario que contiene la información sobre el tamaño y la posición donde colocar la imagen, a la vez de la ruta con el nombre de la imagen.
    - zona: String que indica que lugar de la propia plantilla modificaria

    """

def actualizar_vista_previa(collage, diccionario_para_collage, zona):
    archivo_imagen = traer_imagen(diccionario_para_collage[zona]['ruta'])
    if (archivo_imagen != None):
        imagen_cargada = Pil_image.open(archivo_imagen)
        imagen_seteada = Pil_imageOps.fit(imagen_cargada, (diccionario_para_collage[zona]['ancho'], diccionario_para_collage[zona]['alto']))
    
        tupla_posicion = preparar_posicion(diccionario_para_collage[zona]['posicion'])
        collage.paste(imagen_seteada, tupla_posicion)
    else:
        sg.popup_ok("Ingrese una imagen para agregar al collage") 

"""
    En base al string recibido por parámetro, extrae el caracter de la zona correspondiente y lo devuelve

    Parametros:
    - valor_selectires: String con el nombre completo del "value" que recibe el loop de la ventana de PySimpleGUI
    
    Devuevle:
    - String: Con el caracter correspondiente a la zona recibida por parámetro

    """

def extraer_zona(valor_selectores):
    for clave, valor in valor_selectores.items():
        if (valor == True) and (clave != "-INPUT-"):
            return clave.split('_')[1][0]

"""
    En base al string recibido por parámetro, genera una tupla de ints

    Parametros:
    - string: String con los valores para ser convertido en una tupla
    
    Devuevle:
    - Tuple: Tupla con los valores separados del string recibido por parámetro

    """
 
def preparar_posicion(string):
    nueva_tupla = tuple(map(int, string.split(', ')))
    return nueva_tupla

"""
    Recibiendo el elemento Imagen de Pillow y el string del nuevo titulo, se asigna dicho titulo y se coloca en la imagen

    Parametros:
    - image: Elemento Image de Pillow
    - titulo_nuevo: String con el nuevo titulo para el collage

    """

def actualizar_titulo(image, titulo_nuevo):
    dibujar = Pil_imageDraw.Draw(image)

    largo_titulo = len(titulo_nuevo)

    ancho_marco = 150
    if (largo_titulo > 20):
        ancho_marco = 250

    dibujar.rectangle(
   (15, 375, ancho_marco, 395),
   fill=(255, 255, 255),
   outline=(0, 0, 0))

    dibujar.text((20, 380), titulo_nuevo, fill="black")

####################### FUNCIONES DE MANEJO DE ARCHIVOS #######################

"""
    Genera el string con la ruta completa de la imagen, basandose en el nombre que viene por parámetro

    Parametros:
    - nombre_imagen: String con nombre de la imagen con extension
    
    Devuelve:
    - file: string con la ruta completa de la imagen

    """

def traer_imagen (nombre_imagen):

    ruta_imagenes = os.path.join('UNLPImage', 'imagenes', 'imagenes_collages')

    for filename in os.listdir(ruta_imagenes):

        if (filename == nombre_imagen):
            file = os.path.join(ruta_imagenes, filename)
            return file
        
def _plantillas():

    """
    Genera una lista de plantillas de botones con imagenes.

    Retorna:
    - plantillas: Una lista de plantillas de botones con imágenes.

    """

    plantillas = []
    ruta_imagenes = os.path.join('UNLPImage', 'imagenes', 'plantillas')


    ## Armar funcion que "valide" las plantillas existentes

    for i in range(len(os.listdir(ruta_imagenes))):
        
        nombre_archivo = f'p{i+1}.png'

        if (os.path.isfile(f'{ruta_imagenes}/p{i+1}.png') and (traer_datos_plantilla_json(nombre_archivo, 'ruta'))):
            plantilla = [sg.Button(button_text="", key=f'p{i+1}',image_filename=f'{ruta_imagenes}/p{i+1}.png', image_size=(100, 100))]
            plantillas.append(plantilla)

    return plantillas


def _imagenes():

    """
    Genera una lista de botones con imágenes a partir de los archivos de imágenes en la carpeta 'UNLPImage/imagenes/imagenes_collages' y si tiene, o no, tags asignados en el CSV de la carpet a'UNLPIMage/archivos/datos_imagenes.csv'.

    Retorna:
    - imagenes: Una lista de botones con imágenes.

    """

    ruta_imagenes = os.path.join('UNLPImage', 'imagenes', 'imagenes_collages')

    imagenes = []

   
    for filename in os.listdir(ruta_imagenes):

        ruta_completa = os.path.join(ruta_imagenes, filename)

        if (len(recuperar_tags(ruta_completa)) > 0):
            file = ruta_completa
            imagen = [sg.Button(button_text="", key=f"{filename}", image_filename=file, image_size=(120, 120))]
            imagenes.append(imagen)
    return imagenes

def validar_nombre(nombre_collage):

    """
    Recorre las imágenes de collages en la carpeta 'UNLPImage/imagenes/collages_guardados' y devuelve True o False si encuentra un archivo con el mismo nombre que el parametro.

    Retorna:
    - nombre_collage: Nombre del archivo.

    """
    ruta_collages = os.path.join('UNLPImage', 'imagenes', 'collages_guardados')
   
    for filename in os.listdir(ruta_collages):
        extraer_nombre_archivo = (filename.split('.')[0])
        
        if(nombre_collage == extraer_nombre_archivo):
            return False
        
    return True

####################### FUNCIONES DE GENERACION DE LOGS #######################

"""
    Trae el string con los nombre de imágenes del collage y lo envía al log de movimientos 

    Parametros:
    - alias: String con nombre del usuario
    - collage: Objeto Collage con la información contenida de dicho collage

    """

def enviar_informacion_al_csv(alias, collage):
    valores_para_csv = collage.imprimir_nombre_imagenes()
    insertar_log(alias, "nuevo_collage", valores_para_csv, collage.titulo)

####################### FUNCIONES EXTRAS #######################

"""
    Genera el string de funcionalidades y lo pone en un elemento de tipo Popup

    """

def mostrar_popup_funcionalidades():
    mensaje = '''Bienvenido al Generador de Collage de 'UNLPImage'.

    En la ventana de creación de collage vas a encontrar distintas áreas, lo primero que vas a encontrar es el campo de elección de titulo:
        - Aquí podrás escribir el nombre para tu collage y enviarlo al mismo mediante el botón 'Actualizar'

    Luego, de izquierda a derecha vas a encontrar:
        - Selector de imagen para el collage: es importante aclarar que solo van a aparecer imágenes que SI posean etiquetas asignadas
        - Selector de zona para la imagen: cada plantilla tiene lugares definidos donde van a pegarse cada imgen, vas a poder elegir cada una en esta área
        - Vista previa: en esta área vas a poder ir viendo sincrónicamente cómo va quedando tu collage

    Finalmente en la parte inferior vas a encontrar los botones de:
        - Volver: Para volver a la selección de plantilla haces clic en "Volver".
        - Actualizar: Es preciso que hagas clic en este botón para enviar la información que indiques a la vista previa, de esta forma, el estado de tu collage
        lo vas a poder ir revisando en el area de "Vista previa" antes de guardarlo
        - Guardar: Haciendo clic en este botón, tu collage va a guardarse en nuestro programa 'UNLPImage' con el nombre que le asignaste de título

    '''

    sg.popup('Creación de collage', mensaje)    


def mostrar_popup_nombre_ocupado():
    e = 'El nombre del collage ya existe, escriba otro y haga clic en "Actualizar"'
    sg.popup_ok(e)

"""
    Muestra en pantalla el nombre con el cual se guardaría el collage para confirmar, y en caso de aceptar, valida su unicidad

    """

def confirmar_nombre_collage(nombre_collage):

    ch = sg.popup_yes_no(f'Vas a guardar el collage con el nombre "{nombre_collage}", es correcto?', title="YesNo")    
    if (ch == "Yes"):
        nombre_valido = validar_nombre(nombre_collage)
        if (not nombre_valido):
            mostrar_popup_nombre_ocupado()
            return False
        return True
    else:
        return False
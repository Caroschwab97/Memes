import PySimpleGUI as sg
from matplotlib.figure import Figure
import os
import pandas as pd

from UNLPImage.graficos.constante import ruta_archivo_perfiles,ruta_archivo_img
from UNLPImage.graficos.generar_ventana import crear_ventana

def generate_plot():
    
    try:
        perfiles_data = pd.read_json(ruta_archivo_perfiles)

        # Crear el DataFrame de perfiles
        df_perfiles = pd.DataFrame(perfiles_data)

        # Leer el archivo CSV de imágenes
        df_imagenes = pd.read_csv(ruta_archivo_img)

        # Convertir la columna 'size' a tipo entero
        df_imagenes['size'] = df_imagenes['size'].astype(int)

        # Calcular el tamaño en bytes promedio de las imágenes actualizadas por cada perfil

        # Agrupar por perfil y calcular el promedio del tamaño de las imágenes, y ordenar los resultados
        promedio_tamanio = df_imagenes.groupby('ultimo_perfil')['size'].mean()
        promedio_tamanio = promedio_tamanio.sort_values(ascending=False)

        # Incluir los perfiles que no hayan realizado actualizaciones
        promedio_tamanio = pd.merge(df_perfiles, promedio_tamanio, how='left', left_on='nick', right_index=True)

        # Rellenar los valores faltantes con 0
        promedio_tamanio['size'] = promedio_tamanio['size'].fillna(0)

        # Ordenar tanto los valores como los índices del DataFrame
        promedio_tamanio = promedio_tamanio.sort_index()

        figure = Figure(figsize=(8, 5))  # Ajustar el tamaño de la figura

        colores = ['blue', 'green', 'red', 'orange', 'purple', 'yellow', 'cyan']

        axes = figure.add_subplot()
        axes.bar(promedio_tamanio['nick'], promedio_tamanio['size'],color=colores)
        axes.set_xlabel('Perfil')
        axes.set_ylabel('Tamaño promedio (bytes)')
        axes.set_title('Tamaño promedio de imágenes actualizadas por perfil')
        axes.set_xticklabels(promedio_tamanio['nick'], rotation=90)  # Rotar las etiquetas del eje x si es necesario
        

    except FileNotFoundError:
        figure = Figure(figsize=(8,5))  # Ajustar el tamaño de la figura
        axes = figure.add_subplot()
        nombre_archivo = os.path.basename(ruta_archivo_perfiles)
        axes.text(0.5, 0.5, f"El archivo {nombre_archivo} no se encontro", 
                  horizontalalignment='center', verticalalignment='center',
                  fontsize=14, color='red')

    return figure

def grafico_barras_bytes():
    figura = generate_plot()
    crear_ventana(figura)
import PySimpleGUI as sg
from matplotlib.figure import Figure
import os
import pandas as pd
import re

from UNLPImage.graficos.constante import ruta_archivo_img
from UNLPImage.graficos.generar_ventana import crear_ventana

def generate_plot():

    try:
        datos_img = pd.read_csv(ruta_archivo_img)

        anchos = []
        altos = []

        for resolucion in datos_img['resolucion']:
            match = re.search(r'\((\d+), (\d+)\)', resolucion)
            if match:
                ancho = int(match.group(1)) # hace el match para ancho
                alto = int(match.group(2)) # hace el match para alto
                anchos.append(ancho)
                altos.append(alto)

        figure = Figure(figsize=(8, 5))  # Ajustar el tamaño de la figura

        axes = figure.add_subplot()
        axes.scatter(anchos, altos, s=50, alpha=0.7)  # Crear el grafico de dispersion
        axes.set_xlabel('Ancho')  # Etiqueta del eje x
        axes.set_ylabel('Alto')  # Etiqueta del eje y
        axes.set_title('Relacion entre Ancho y Alto de las Imagenes (en pixeles)')
        #axes.axis('off')

    except FileNotFoundError:
        figure = Figure(figsize=(8,5))  # Ajustar el tamaño de la figura
        axes = figure.add_subplot()
        nombre_archivo = os.path.basename(ruta_archivo_img)
        axes.text(0.5, 0.5, f"El archivo {nombre_archivo} no se encontro", 
                  horizontalalignment='center', verticalalignment='center',
                  fontsize=14, color='red')

    return figure


def grafico_dispersion():
    figura = generate_plot()
    crear_ventana(figura)
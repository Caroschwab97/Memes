import PySimpleGUI as sg
from matplotlib.figure import Figure
import os
import pandas as pd

from UNLPImage.graficos.constante import ruta_archivo
from UNLPImage.graficos.generar_ventana import crear_ventana

def generate_plot():

    try:
        logs_df = pd.read_csv(ruta_archivo)

        count = logs_df['operacion'].value_counts()

        figure = Figure(figsize=(8,5))  # Ajustar el tamaño de la figura

        axes = figure.add_subplot()
    
        # Crear un grafico de tipo pastel con los resultados
        axes.pie(count, labels=count.index, autopct='%1.1f%%')

        # Establecer el titulo del grafico
        axes.set_title('Cantidades de cada operación realizada')
        figure.subplots_adjust(left=0.0, right=0.85)

    except FileNotFoundError:
        figure = Figure(figsize=(8,5))  # Ajustar el tamaño de la figura
        axes = figure.add_subplot()
        nombre_archivo = os.path.basename(ruta_archivo)
        axes.text(0.5, 0.5, f"El archivo {nombre_archivo} no se encontro", 
                  horizontalalignment='center', verticalalignment='center',
                  fontsize=14, color='red')

    return figure


def grafico_torta():
    figura = generate_plot()
    crear_ventana(figura)
import PySimpleGUI as sg
from matplotlib.figure import Figure
import numpy as np
import os
import pandas as pd

from UNLPImage.graficos.constante import ruta_archivo
from UNLPImage.graficos.generar_ventana import crear_ventana

def generate_plot():

    try:
        logs_df = pd.read_csv(ruta_archivo)

        logs_df['timestamp'] = pd.to_datetime(logs_df['timestamp'])

        logs_df['DiaSemana'] = logs_df['timestamp'].dt.day_name()

        count = logs_df['DiaSemana'].value_counts()

        colores = ['blue', 'green', 'red', 'orange', 'purple', 'yellow', 'cyan']
 
        figure = Figure(figsize=(8,5))  # Ajustar el tamaño de la figura
        axes = figure.add_subplot()
        axes.bar(count.index, count.values, color=colores)
        axes.set_xlabel('Día de la semana')
        axes.set_ylabel('Cantidad de operaciones')
        axes.set_title('Distribución de operaciones por día de la semana')

        # Establecer las ubicaciones y etiquetas del eje x
        xticks = np.arange(len(count))
        axes.set_xticks(xticks)
        axes.set_xticklabels(count.index, rotation=30, ha= 'right')
        figure.subplots_adjust(top=0.90, bottom=0.2)
        
    except FileNotFoundError:
        figure = Figure(figsize=(8,5))  # Ajustar el tamaño de la figura
        axes = figure.add_subplot()
        nombre_archivo = os.path.basename(ruta_archivo)
        axes.text(0.5, 0.5, f"El archivo {nombre_archivo} no se encontro", 
                  horizontalalignment='center', verticalalignment='center',
                  fontsize=14, color='red')
        
    return figure


def grafico_barra_vertical():
    figura = generate_plot()
    crear_ventana(figura)
    
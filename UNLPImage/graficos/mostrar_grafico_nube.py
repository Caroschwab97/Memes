import PySimpleGUI as sg
from matplotlib.figure import Figure
from wordcloud import WordCloud
import os
import pandas as pd

from UNLPImage.graficos.constante import ruta_archivo
from UNLPImage.graficos.generar_ventana import crear_ventana

# Funcion para generar el grafico utilizando pandas y matplotlib
def generate_plot():

    try:
        logs_df = pd.read_csv(ruta_archivo)

        textos_memes = logs_df[logs_df['operacion'] == 'nuevo_meme']['textos'].dropna().tolist()

        figure = Figure(figsize=(8,5))  # Ajustar el tamaño de la figura

        axes = figure.add_subplot()

        if not textos_memes:
            textos_memes = ['sin_texto']

        wordcloud_memes = WordCloud(width=900, height=600, background_color='black').generate(' '.join(textos_memes))

        axes.imshow(wordcloud_memes, interpolation='bilinear')
        axes.set_title('Nube de palabras - Memes')
        axes.axis('off')
        figure.subplots_adjust(left=0.02, right=0.98, top=0.92, bottom=0.05)

    except FileNotFoundError:
        figure = Figure(figsize=(8,5))  # Ajustar el tamaño de la figura
        axes = figure.add_subplot()
        nombre_archivo = os.path.basename(ruta_archivo)
        axes.text(0.5, 0.5, f"El archivo {nombre_archivo} no se encontro", 
                  horizontalalignment='center', verticalalignment='center',
                  fontsize=14, color='red')

    return figure


def grafico_nube():
    figura = generate_plot()
    crear_ventana(figura)
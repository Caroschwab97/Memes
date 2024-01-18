import PySimpleGUI as sg
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def crear_ventana(figura):
    # Crear la ventana de PySimpleGUI
    window = sg.Window(title='Grafico',
                   layout=[[sg.Text(key='title')],
                           [sg.Canvas(key='canvas', size=(800, 560))]],
                    finalize=True)

    # Obtencion del canvas
    canvas = window['canvas'].TKCanvas

    # Crear el lienzo de Matplotlib para mostrarlo en PySimpleGUI
    figure_canvas_agg = FigureCanvasTkAgg(figura, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)


    # Bucle principal de eventos de PySimpleGUI
    while True:
        event, values = window.read() 

        if event == sg.WINDOW_CLOSED:
            break

    window.close()
import os
import csv
import datetime

def insertar_log(alias, operacion="NO OPERATION DATA", valores='', textos=''):
    """
    Inserta un registro de log en un archivo CSV.

    :param alias: Alias relacionado con la operación.
    :param operacion: Descripción de la operación realizada (opcional).
    """

    # Nombres de las columnas para el archivo CSV
    nombres_columnas = ["timestamp", "nick", "operacion", "valores", "textos"]

    try:
        # Construye la ruta de archivo utilizando os.path.join()
        ruta_archivo = os.path.join('UNLPImage', 'archivos', 'logs.csv')

        # Verifica si el archivo existe
        archivo_existe = os.path.exists(ruta_archivo)

        with open(ruta_archivo, mode='a', newline="") as archivo_csv:
            writer = csv.writer(archivo_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            # Escribe los nombres de las columnas si el archivo es recién creado
            if not archivo_existe:
                writer.writerow(nombres_columnas)

            writer.writerow([datetime.datetime.now(), alias, operacion, valores, textos])

    except PermissionError:
        print("No se tienen permisos para acceder al archivo de logs.")
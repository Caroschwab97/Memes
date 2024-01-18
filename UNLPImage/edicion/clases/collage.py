class Collage:

    def __init__(self, espacios, lugares, ruta):
        self.espacios = espacios
        self.ruta = ruta
        self.lugares = lugares
        self.titulo = ""
    
    def imprimir_lugares(self) -> str:
        print(self.lugares.items())

    def sumar_imagen_en_posicion(self, zona, imagen_filename):
        self.lugares[zona]['ruta'] = imagen_filename

    def definir_titulo(self, titulo_ingresado):
        self.titulo = titulo_ingresado

    def generar_filename(self):
        try:
            filename = self.titulo.replace(' ', '_')
            return filename
        except ValueError:
            print("El titulo no está definido")
        
    def imprimir_nombre_imagenes(self) -> str:
        string_final = ""
        for valor in self.lugares.values():
            if 'ruta' in valor:
                string_final = string_final + (f'{valor["ruta"]};')
        return string_final
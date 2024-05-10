class Nodo:
    def __init__(self, nombre, tipo):
        self.nombre = nombre  # Nombre del directorio o archivo
        self.tipo = tipo  # Tipo: 'directorio' o 'archivo'
        self.hijos = []  # Lista de hijos (subdirectorios o archivos)

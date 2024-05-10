from flask import render_template, request, redirect, url_for
from .clases.nodo import Nodo
from . import actArbolesBP

# Función para construir un árbol de ejemplo
def construir_arbol():
    raiz = Nodo('raiz', 'directorio')

    #Creacion de carpetas
    carpeta1 = Nodo('carpeta1', 'directorio')
    carpeta2 = Nodo('carpeta2', 'directorio')
    archivo1 = Nodo('archivo1.txt', 'archivo')
    archivo2 = Nodo('archivo2.txt', 'archivo')

    subCarpeta1 = Nodo('subCarpeta1', 'directorio')
    subCarpeta2 = Nodo('subCarpeta2', 'directorio')
    subCarpeta3 = Nodo('subCarpeta3', 'directorio')
    subCarpeta4 = Nodo('subCarpeta4', 'directorio')

    raiz.hijos.append(carpeta1)
    raiz.hijos.append(carpeta2)
    carpeta1.hijos.append(archivo1)
    carpeta1.hijos.append(subCarpeta1)
    carpeta2.hijos.append(archivo2)
    carpeta2.hijos.append(subCarpeta2)
    carpeta2.hijos.append(subCarpeta4)

    return raiz

arbol_ejemplo = construir_arbol()

@actArbolesBP.route('/act_arboles', methods=['GET', 'POST'])
def actArboles():
    global arbol_ejemplo
    if request.method == 'POST':
        nombre = request.form['nombre']
        tipo = request.form['tipo']
        nuevo_nodo = Nodo(nombre, tipo)
        arbol_ejemplo.hijos.append(nuevo_nodo)
        return render_template('trabajos/arboles.html', arbol=arbol_ejemplo) 
    return render_template('trabajos/arboles.html', arbol=arbol_ejemplo)
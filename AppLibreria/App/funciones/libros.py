from flask import render_template, request
import json

from . import librosBP

#Mostrar Pagina principal de Libros
@librosBP.route('/')
def librosPage():
    with open('App/funciones/libros.txt', 'r') as file:
        libros = json.load(file)
    return render_template('vistas/libros.html', libros=libros)

# Búsqueda de los libros
@librosBP.route('/buscar_libro', methods=['POST'])
def buscar_libro():
    termino_busqueda = request.form['buscar'].lower()
    with open('App/funciones/libros.txt', 'r') as file:
        libros = json.load(file)

    #  
    libros_encontrados = [libro for libro in libros if termino_busqueda == libro['Titulo'].lower()]

    if libros_encontrados:
        libro_no_encontrado = False
    else:
        libro_no_encontrado = True

    return render_template('vistas/libros.html', libros=libros_encontrados, libro_no_encontrado=libro_no_encontrado)

#Crear o agregar un nuevo lirbo
@librosBP.route('/agregar_libro', methods=['POST'])
def agregar_libro():
    nuevo_libro = {
        "Titulo": request.form['titulo'],
        "Autor": request.form['autor'],
        "Editorial": request.form['editorial'],
        "ISBN": request.form['isbn'],
        "Cantidad_Disponible": int(request.form['cantidad'])
    }
    print(type(nuevo_libro))
    with open('App/funciones/libros.txt', 'r') as file:
        libros = json.load(file)
        print(type(libros))
    libros.append(nuevo_libro)
    with open('App/funciones/libros.txt', 'w') as file:
        json.dump(libros, file, indent=4)
    return render_template('vistas/libros.html', libros=libros)

#Elimina un libro existente
@librosBP.route('/eliminar_libro', methods=['POST'])
def eliminar_libro():
    id_libro = request.form['id_libro']
    with open('App/funciones/libros.txt', 'r') as file:
        libros = json.load(file)
    # Agarra el ID del libro a eliminar y en la lista itera y pasa todos los libros menos el del id a rellenar
    libros = [libro for libro in libros if libro['Titulo'] != id_libro]
    with open('App/funciones/libros.txt', 'w') as file:
        json.dump(libros, file, indent=4)
    return render_template('vistas/libros.html', libros=libros  )

from flask import render_template, request, redirect, url_for
import json

from . import librosBP

#Mostrar Pagina principal de Libros
@librosBP.route('/')
def librosPage():
    with open('App/funciones/libros.txt', 'r') as file:
        libros = json.load(file)
    return render_template('vistas/libros.html', libros=libros)

#Busqueda de los libros
@librosBP.route('/buscar_libro', methods=['POST'])
def buscar_libro():
    termino_busqueda = request.form['buscar'].lower()
    with open('App/funciones/libros.txt', 'r') as file:
        libros = json.load(file)
    libros_encontrados = [libro for libro in libros if termino_busqueda in libro['Titulo'].lower()]
    return render_template('vistas/libros.html', libros=libros_encontrados)

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
    with open('App/funciones/libros.txt', 'r') as file:
        libros = json.load(file)
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
    libros = [libro for libro in libros if libro['Titulo'] != id_libro]
    with open('App/funciones/libros.txt', 'w') as file:
        json.dump(libros, file, indent=4)
    return render_template('vistas/libros.html', libros=libros  )
from flask import render_template, request, redirect, url_for
from datetime import datetime
import json

from . import prestamosBP

@prestamosBP.route('/prestamos')
def prestamosPage():
    with open('App/funciones/prestamos.txt', 'r') as file:
        prestamos = json.load(file)
    with open('App/funciones/libros.txt', 'r') as file:
        libros = json.load(file)
    with open('App/funciones/usuarios.txt', 'r') as file:
        usuarios = json.load(file)
    return render_template('vistas/prestamos.html', prestamos=prestamos, libros=libros, usuarios=usuarios)

# Ruta para procesar un nuevo préstamo
@prestamosBP.route('/prestamo', methods=['POST'])
def realizar_prestamo():
    nom_libro = str(request.form['nom_libro'])
    nom_usuario = str(request.form['nom_usuario'])
    fecha_prestamo = datetime.now().strftime('%Y-%m-%d')
    
    nuevo_prestamo = {
        "ID_Prestamo": obtener_nuevo_id_prestamo(),
        "Titulo": nom_libro,
        "ID_Usuario": nom_usuario,
        "Fecha_Prestamo": fecha_prestamo,
        "Fecha_Devolucion": ""
    }
    
    with open('App/funciones/prestamos.txt', 'r') as file:
        prestamos = json.load(file)
    prestamos.append(nuevo_prestamo)
    with open('App/funciones/prestamos.txt', 'w') as file:
        json.dump(prestamos, file, indent=4)
    with open('App/funciones/libros.txt', 'r') as file:
        libros = json.load(file)
    with open('App/funciones/usuarios.txt', 'r') as file:
        usuarios = json.load(file)

    return render_template('vistas/prestamos.html', prestamos=prestamos, libros=libros, usuarios=usuarios)

# Ruta para devolver un préstamo
@prestamosBP.route('/devolucion', methods=['POST'])
def devolver_prestamo():
    id_prestamo = int(request.form['id_prestamo'])
    fecha_devolucion = datetime.now().strftime('%Y-%m-%d')
    
    with open('App/funciones/prestamos.txt', 'r') as file:
        prestamos = json.load(file)
    for prestamo in prestamos:
        if prestamo['ID_Prestamo'] == id_prestamo:
            prestamo['Fecha_Devolucion'] = fecha_devolucion
            break
    
    with open('App/funciones/prestamos.txt', 'w') as file:
        json.dump(prestamos, file, indent=4)
    with open('App/funciones/libros.txt', 'r') as file:
        libros = json.load(file)
    with open('App/funciones/usuarios.txt', 'r') as file:
        usuarios = json.load(file)
    
    return render_template('vistas/prestamos.html', prestamos=prestamos, libros=libros, usuarios=usuarios)

# Función para obtener un nuevo ID de préstamo
def obtener_nuevo_id_prestamo():
    with open('App/funciones/prestamos.txt', 'r') as file:
        prestamos = json.load(file)
    if not prestamos:
        return 1
    else:
        ultimo_id = max(prestamos, key=lambda x: x['ID_Prestamo'])['ID_Prestamo']
        return ultimo_id + 1
from flask import render_template, request, redirect, url_for
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

# Ruta para realizar un préstamo
@prestamosBP.route('/realizar_prestamo', methods=['POST'])
def realizar_prestamo():
    libro = request.form['libro']
    usuario_id = int(request.form['usuario'])
    fecha_prestamo = request.form['fecha_prestamo']
    fecha_devolucion = request.form['fecha_devolucion']
    
    # Obtener datos del libro y usuario
    with open('App/funciones/libros.txt', 'r') as file:
        libros = json.load(file)
    libro_id = None
    for libro_info in libros:
        if libro_info['Titulo'] == libro:
            libro_id = libro_info['ID_Libro']
            break
    
    # Crear el nuevo préstamo
    nuevo_prestamo = {
        "ID_Prestamo": obtener_nuevo_id_prestamo(),  # Obtener un nuevo ID para el préstamo
        "ID_Libro": libro_id,
        "ID_Usuario": usuario_id,
        "Fecha_Prestamo": fecha_prestamo,
        "Fecha_Devolucion": fecha_devolucion
    }
    
    # Guardar el nuevo préstamo en el archivo prestamos.txt
    with open('App/funciones/prestamos.txt', 'r') as file:
        prestamos = json.load(file)
    prestamos.append(nuevo_prestamo)
    with open('App/funciones/prestamos.txt', 'w') as file:
        json.dump(prestamos, file, indent=4)
    
    return redirect(url_for('prestamosPage'))

# Función para obtener un nuevo ID para el préstamo
def obtener_nuevo_id_prestamo():
    with open('App/funciones/prestamos.txt', 'r') as file:
        prestamos = json.load(file)
    if not prestamos:
        return 1
    else:
        ultimo_id = max(prestamos, key=lambda x: x['ID_Prestamo'])['ID_Prestamo']
        return ultimo_id + 1


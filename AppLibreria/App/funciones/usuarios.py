from flask import render_template, request
import json

from . import usuariosBP

@usuariosBP.route('/usuarios')
def prestamosPage():
    with open('App/funciones/usuarios.txt', 'r') as file:
        usuarios = json.load(file)
    return render_template('vistas/usuarios.html', usuarios=usuarios)

# Ruta para procesar la búsqueda de usuarios
@usuariosBP.route('/buscar_usuario', methods=['POST'])
def buscar_usuario():
    termino_busqueda = request.form['buscar'].lower()
    with open('App/funciones/usuarios.txt', 'r') as file:
        usuarios = json.load(file)
    usuarios_encontrados = [usuario for usuario in usuarios if termino_busqueda in usuario['Nombre'].lower()]
    return render_template('vistas/usuarios.html', usuarios=usuarios_encontrados)

# Función para obtener un nuevo ID para el usuario
def obtener_nuevo_id():
    with open('App/funciones/usuarios.txt', 'r') as file:
        usuarios = json.load(file)
    if not usuarios:
        return 1
    else:
        ultimo_id = max(usuarios, key=lambda x: x['ID_Usuario'])['ID_Usuario']
        return ultimo_id + 1

# Ruta para agregar un nuevo usuario
@usuariosBP.route('/agregar_usuario', methods=['POST'])
def agregar_usuario():
    nuevo_usuario = {
        "ID_Usuario": obtener_nuevo_id(),  # Obtener un nuevo ID para el usuario
        "Nombre": request.form['nombre'],
        "Apellido": request.form['apellido'],
        "Correo_Electronico": request.form['correo'],
        "Telefono": request.form['telefono']
    }
    with open('App/funciones/usuarios.txt', 'r') as file:
        usuarios = json.load(file)
    usuarios.append(nuevo_usuario)
    with open('App/funciones/usuarios.txt', 'w') as file:
        json.dump(usuarios, file, indent=4)
    return render_template('vistas/usuarios.html', usuarios=usuarios)

# Ruta para eliminar un usuario
@usuariosBP.route('/eliminar_usuario', methods=['POST'])
def eliminar_usuario():
    id_usuario = int(request.form['id_usuario'])
    with open('App/funciones/usuarios.txt', 'r') as file:
        usuarios = json.load(file)
    usuarios = [usuario for usuario in usuarios if usuario['ID_Usuario'] != id_usuario]
    with open('App/funciones/usuarios.txt', 'w') as file:
        json.dump(usuarios, file, indent=4)
    return render_template('vistas/usuarios.html', usuarios=usuarios)

# Ruta para actualizar un usuario
@usuariosBP.route('/actualizar_usuario', methods=['POST'])
def actualizar_usuario():
    id_usuario = int(request.form['id_usuario'])
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    correo = request.form['correo']
    telefono = request.form['telefono']
    
    with open('App/funciones/usuarios.txt', 'r') as file:
        usuarios = json.load(file)
    
    for usuario in usuarios:
        if usuario['ID_Usuario'] == id_usuario:
            usuario['Nombre'] = nombre
            usuario['Apellido'] = apellido
            usuario['Correo_Electronico'] = correo
            usuario['Telefono'] = telefono
            break
    
    with open('App/funciones/usuarios.txt', 'w') as file:
        json.dump(usuarios, file, indent=4)
    
    return render_template('vistas/usuarios.html', usuarios=usuarios) 


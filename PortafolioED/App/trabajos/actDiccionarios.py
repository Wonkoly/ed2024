from flask import render_template, redirect, request, url_for
from . import actDiccionariosBP

usuarios = [
    {'id': 1, 'nombre': 'Usuario 1', 'email': 'usuario1@example.com'},
    {'id': 2, 'nombre': 'Usuario 2', 'email': 'usuario2@example.com'},
    {'id': 3, 'nombre': 'Usuario 3', 'email': 'usuario3@example.com'}
]

@actDiccionariosBP.route('/act_diccionarios',methods=['GET', 'POST'])
def actDiccionarios():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        nuevo_usuario = {'id': len(usuarios) + 1, 'nombre': nombre, 'email': email}
        usuarios.append(nuevo_usuario)
        return redirect(url_for('actDiccionarios.actDiccionarios'))
    return render_template('trabajos/diccionarios.html', usuarios=usuarios)

@actDiccionariosBP.route('/eliminar_usuario/<int:usuario_id>', methods=['GET'])
def eliminar_usuario(usuario_id):
    global usuarios
    usuarios = [usuario for usuario in usuarios if usuario['id'] != usuario_id]     
    return redirect(url_for('actDiccionarios.actDiccionarios'))
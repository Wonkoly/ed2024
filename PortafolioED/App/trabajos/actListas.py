from flask import render_template, request, redirect, url_for

from . import actListasBP

elementos = []

@actListasBP.route('/act_listas', methods=['GET', 'POST'])
def actListas():
    if request.method == 'POST':
        elemento = request.form['elemento']
        if elemento:
            elementos.append(elemento)
    return render_template('trabajos/listas.html', elementos=elementos)

@actListasBP.route('/eliminar/<int:index>', methods=['GET'])
def eliminar_elemento(index):
    if index >= 0 and index < len(elementos):
        elementos.pop(index) 
    return redirect(url_for('actListas.actListas'))


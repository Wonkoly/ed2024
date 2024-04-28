from flask import render_template

from . import librosBP

@librosBP.route('/')
def librosPage():
    return render_template('vistas/libros.html')
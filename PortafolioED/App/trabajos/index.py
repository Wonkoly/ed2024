from flask import render_template

from . import indexBP

@indexBP.route('/')
@indexBP.route('/index')
def index():
    return render_template('vistas/index.html')

@indexBP.route('/trabajos')
def trabajos_index():
    return render_template('vistas/trabajos.html')

@indexBP.route('/info')
def info_index():
    return render_template('vistas/info.html')
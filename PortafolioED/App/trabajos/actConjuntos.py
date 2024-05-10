from flask import render_template, redirect, request
from . import actConjuntosBP

@actConjuntosBP.route('/act_conjuntos', methods=['GET', 'POST'])
def actConjuntos():
    if request.method == 'POST':
        try:
            conjunto_a = set(map(int, request.form['conjunto_a'].split(',')))
            conjunto_b = set(map(int, request.form['conjunto_b'].split(',')))
        except ValueError:
            return render_template('trabajos/conjuntos.html', error="Ingrese números separados por comas.")

        operacion = request.form['operacion']
        resultado = None
        if operacion == 'union':
            resultado = conjunto_a.union(conjunto_b)
        elif operacion == 'interseccion':
            resultado = conjunto_a.intersection(conjunto_b)
        elif operacion == 'diferencia':
            resultado = conjunto_a.difference(conjunto_b)
        elif operacion == 'pertenencia':
            elemento = int(request.form['elemento'])
            resultado = elemento in conjunto_a
        return render_template('trabajos/conjuntos.html', resultado=resultado)
    return render_template('trabajos/conjuntos.html', resultado=None, error=None)
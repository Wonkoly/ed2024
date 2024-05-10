from flask import render_template, redirect, request, jsonify
import re
from .clases.tupla import Tupla
from . import actTuplasBP

tupla = Tupla()

@actTuplasBP.route('/act_tuplas', methods=["GET", "POST"])
def actTuplas():
    if request.method == "POST":
        sexo = request.form["sexo"]
        nombre = request.form["nombre"]
        cura = request.form["cura"]
        latitud = request.form["latitud"]
        longitud = request.form["longitud"]
        fecha_nacimiento = request.form["fecha_nacimiento"]

        # Validar que latitud y longitud sean números
        if not es_numero(latitud) or not es_numero(longitud):
            return "Error: La latitud y la longitud deben ser números."

        # Validar que el sexo sea Masculino, Femenino o CamionTracktor
        if sexo not in ["Masculino", "Femenino", "NoBinario"]:
            return "Error: El sexo debe ser Masculino, Femenino."

        data = (sexo, nombre, cura, latitud, longitud, fecha_nacimiento)
        tupla_datos = tupla.save_tuple(data)
        return jsonify(tupla_datos)
    return render_template("trabajos/tuplas.html")

def es_numero(valor):
    # Utilizar expresión regular para verificar si el valor es un número
    return bool(re.match(r'^-?\d+(\.\d+)?$', valor))

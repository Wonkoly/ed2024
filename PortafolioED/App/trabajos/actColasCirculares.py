from flask import render_template, request, redirect, url_for
from . import actColasCircularesBP

from .clases.circularQueue import CircularQueue

cola_turnos = CircularQueue(10)
pacientes_atendidos = []

@actColasCircularesBP.route('/act_colascirculares', methods=['GET', 'POST'])
def actColascirculares():
    if request.method == 'POST':
        nombre_paciente = request.form['nombre']
        if nombre_paciente:
            try:
                cola_turnos.enqueue(nombre_paciente)
            except Exception as e:
                return str(e)
    return render_template('trabajos/colasCirculares.html', turnos=cola_turnos.queue, atendidos=pacientes_atendidos)


@actColasCircularesBP.route('/atender_turno', methods=['POST'])
def atender_turno():
    try:
        paciente_atendido = cola_turnos.dequeue()
        pacientes_atendidos.append(paciente_atendido) 
    except Exception as e:
        return str(e)
    return redirect(url_for('actColasCirculares.actColascirculares'))
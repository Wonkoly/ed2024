from flask import render_template, redirect, request, url_for
from datetime import datetime
from . import actPilasBP

tasks = []

@actPilasBP.route('/act_pilas')
def actPilas():
    return render_template('trabajos/pilas.html', tasks=tasks)

@actPilasBP.route('/add_task', methods=['POST'])
def add_task():
    task_name = request.form['task_name']
    description = request.form['description']
    end_date = request.form['end_date']

    # Obtener la fecha de inicio actual
    start_date = datetime.now().strftime('%Y-%m-%d')

    task = {
        'name': task_name,
        'description': description,
        'start_date': start_date,
        'end_date': end_date if end_date else None
    }

    tasks.append(task)
    return redirect(url_for('actPilas.actPilas')) 

@actPilasBP.route('/delete_tasks', methods=['POST'])
def delete_tasks():
    selected_indexes = request.form.getlist('selected_tasks')
    selected_indexes = [int(index) for index in selected_indexes]
    selected_indexes.sort(reverse=True)  # Eliminar desde el final para evitar problemas de índices cambiantes
    for index in selected_indexes:
        del tasks[index]
    return redirect(url_for('actPilas.actPilas'))


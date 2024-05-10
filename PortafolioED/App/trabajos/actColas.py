from flask import render_template, request, redirect, url_for
from queue import Queue
from . import actColasBP

# Menú de platos
menu = {
    '1': 'Hamburguesa',
    '2': 'Pizza',
    '3': 'Ensalada',
    '4': 'Pasta',
    '5': 'Sushi',
    '6': 'Tacos'
}

# Cola para almacenar pedidos con nombre de cliente
cola_pedidos = Queue()

@actColasBP.route('/act_colas', methods=['GET', 'POST'])
def actColas():
    if request.method == 'POST':
        # Obtener el pedido y nombre del cliente desde el formulario
        pedido_id = request.form['pedido']
        nombre_cliente = request.form['nombre']
        if pedido_id in menu.keys() and nombre_cliente:
            pedido = f"{nombre_cliente}: {menu[pedido_id]}"
            # Agregar el pedido a la cola
            cola_pedidos.put(pedido)
    
    # Renderizar la plantilla HTML con el menú y la cola de pedidos
    return render_template('trabajos/colas.html', menu=menu, pedidos=list(cola_pedidos.queue))

@actColasBP.route('/servir_pedido', methods=['POST'])
def servir_pedido():
    # Eliminar el primer pedido de la cola (simula que se ha servido)
    cola_pedidos.get()
    return redirect(url_for('actColas.actColas'))
from flask import render_template, request
import networkx as nx
import matplotlib.pyplot as plt
from io import BytesIO
import base64

from . import actGrafosBP

@actGrafosBP.route('/act_grafos', methods=['GET', 'POST'])
def actGrafos():
    imagen_encoded = None
    error_message = None

    if request.method == 'POST':
        matriz = request.form['matriz']

        try:
            grafo = generar_grafo(matriz)
            imagen_grafo = generar_imagen_grafo(grafo)
            imagen_encoded = base64.b64encode(imagen_grafo).decode('utf-8')
        except (ValueError, IndexError, TypeError):
            error_message = 'La matriz de adyacencia ingresada no es válida.'

    return render_template('trabajos/grafos.html', imagen_encoded=imagen_encoded, error_message=error_message)

def generar_grafo(matriz):
    matriz_adyacencia = [list(map(int, fila.split(','))) for fila in matriz.split(';')]
    nodos = range(1, len(matriz_adyacencia) + 1)  # Generar lista de nodos
    bordes = [(i + 1, j + 1) for i in range(len(matriz_adyacencia)) for j in range(len(matriz_adyacencia[i])) if matriz_adyacencia[i][j] == 1]
    grafo = nx.DiGraph()
    grafo.add_nodes_from(nodos)
    grafo.add_edges_from(bordes)
    return grafo

def generar_imagen_grafo(grafo):
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(grafo)
    nx.draw(grafo, pos, with_labels=True, node_size=1000, node_color='lightblue', font_size=10, font_weight='bold', arrows=True)
    plt.axis('off')
    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    return img.getvalue()
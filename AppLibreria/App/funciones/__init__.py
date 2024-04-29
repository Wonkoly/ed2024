from flask import Blueprint

# Creamos los Blueprints de cada modulo de nuestro proyecto
librosBP = Blueprint('libros', __name__, template_folder='templates')
prestamosBP = Blueprint('prestamos', __name__, template_folder='templates')
usuariosBP = Blueprint('usuarios', __name__, template_folder='templates')

# Importamos cada Modulo para tratarlos como Blueprints
from . import libros
from . import prestamos
from . import usuarios

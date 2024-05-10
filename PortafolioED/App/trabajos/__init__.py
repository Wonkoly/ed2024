from flask import Blueprint

#Creacion de blueprints
indexBP = Blueprint('libros', __name__, template_folder='templates')
actListasBP = Blueprint('actListas', __name__, template_folder='templates')
actColasBP = Blueprint('actColas', __name__, template_folder='templates')
actColasCircularesBP = Blueprint('actColasCirculares', __name__, template_folder='templates')
actPilasBP = Blueprint('actPilas', __name__, template_folder='templates')
actArbolesBP = Blueprint('actArboles', __name__, template_folder='templates')
actConjuntosBP = Blueprint('actConjuntos', __name__, template_folder='templates')
actTuplasBP = Blueprint('actTuplas', __name__, template_folder='templates')
actDiccionariosBP = Blueprint('actDiccionarios', __name__, template_folder='templates')
actGrafosBP = Blueprint('actGrafos', __name__, template_folder='templates')

#Importacion de cada modulo para tratarlos como blueprints
from . import index
from . import actListas
from . import actColas
from . import actColasCirculares
from . import actPilas
from . import actArboles
from . import actConjuntos
from . import actTuplas
from . import actDiccionarios
from . import actGrafos


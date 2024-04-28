from flask import Blueprint

librosBP = Blueprint('libros', __name__, template_folder='templates')



from . import libreria
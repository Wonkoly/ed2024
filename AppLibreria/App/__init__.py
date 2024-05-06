from flask import Flask

def create_app():
    app = Flask(__name__)

    #Registro de Blueprins
    from .funciones import librosBP, usuariosBP, prestamosBP

    app.register_blueprint(librosBP)
    app.register_blueprint(usuariosBP)
    app.register_blueprint(prestamosBP)
    
    return app
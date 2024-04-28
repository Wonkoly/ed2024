from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    #Registro de Blueprins
    from .funciones import librosBP
    app.register_blueprint(librosBP)

    return app
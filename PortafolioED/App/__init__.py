from flask import Flask

def create_app():

    app = Flask(__name__)
    
    from .trabajos import indexBP
    from .trabajos import actListasBP
    from .trabajos import actColasBP
    from .trabajos import actColasCircularesBP
    from .trabajos import actPilasBP
    from .trabajos import actArbolesBP
    from .trabajos import actConjuntosBP
    from .trabajos import actTuplasBP
    from .trabajos import actDiccionariosBP
    from .trabajos import actGrafosBP

    #Registro de blueprints
    app.register_blueprint(indexBP)
    app.register_blueprint(actListasBP)
    app.register_blueprint(actColasBP)
    app.register_blueprint(actColasCircularesBP)
    app.register_blueprint(actPilasBP)
    app.register_blueprint(actArbolesBP)
    app.register_blueprint(actConjuntosBP)
    app.register_blueprint(actTuplasBP)
    app.register_blueprint(actDiccionariosBP)
    app.register_blueprint(actGrafosBP)

    return app
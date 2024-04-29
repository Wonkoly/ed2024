from . import db

class Libro(db.Model):
    ID_Libro = db.Column(db.Integer, primary_key=True)
    Titulo = db.Column(db.String(255), nullable=True)
    Autor = db.Column(db.String(255), nullable=True)
    Editorial = db.Column(db.String(255), nullable=True)
    ISBN = db.Column(db.String(20), nullable=True)
    Cantidad_Disponible = db.Column(db.Integer, nullable=True)

class Usuario(db.Model):
    ID_Usuario = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(100), nullable=True)
    Apellido = db.Column(db.String(100), nullable=True)
    Correo_Electronico = db.Column(db.String(255), nullable=True)
    Telefono = db.Column(db.String(15), nullable=True)

class Prestamo(db.Model):
    ID_Prestamo = db.Column(db.Integer, primary_key=True)
    Fecha_Salida = db.Column(db.Date, nullable=True)
    Fecha_Entrega = db.Column(db.Date, nullable=True)
    Estado = db.Column(db.String(50), nullable=True)
    LIBROS_ID_Libros = db.Column(db.Integer, db.ForeignKey('libro.ID_Libro'), nullable=False)
    USUARIOS_ID_Usuario = db.Column(db.Integer, db.ForeignKey('usuario.ID_Usuario'), nullable=False)

    libro = db.relationship('Libro', backref=db.backref('prestamos', lazy=True))
    usuario = db.relationship('Usuario', backref=db.backref('prestamos', lazy=True))

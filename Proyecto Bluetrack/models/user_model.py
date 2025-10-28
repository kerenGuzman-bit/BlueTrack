from database import db

# Definición del modelo de usuario
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    correo = db.Column(db.String(100), unique=True, nullable=False)  # Agregando correo
    nombre = db.Column(db.String(100), nullable=False)  # Agregando nombre
    login = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
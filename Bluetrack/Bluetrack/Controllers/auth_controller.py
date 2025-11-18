from flask import Blueprint, render_template, request, redirect, url_for
from database import db
from models.user_model import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/', methods=['GET', 'POST'])
def index():
    error = ''
    if request.method == 'POST':
        form_login = request.form.get('usuario')
        form_password = request.form.get('contrasena')
        user = User.query.filter_by(login=form_login, password=form_password).first()
        if user:
            return redirect(url_for('paginas.categorias'))
        else:
            error = 'Nombre de usuario o contraseña incorrectos'
    return render_template('index.html', error=error)

@auth_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        correo = request.form['correo']
        nombre = request.form['nombre']
        contrasena = request.form['contrasena']
        confirmar = request.form['confirmar']

        if contrasena != confirmar:
            return "Las contraseñas no coinciden"

        usuario_existente = User.query.filter_by(correo=correo).first()
        if usuario_existente:
            return "El correo ya está registrado"

        nuevo_usuario = User(correo=correo, nombre=nombre, login=correo, password=contrasena)
        db.session.add(nuevo_usuario)
        db.session.commit()

        return redirect(url_for('auth.index'))
    
    return render_template('registro.html')

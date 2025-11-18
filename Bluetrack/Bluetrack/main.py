from flask import Flask
from database import db
from Controllers.auth_controller import auth_bp
from Controllers.paginas_controller import paginas_bp
from Controllers.consumo_controller import consumo_bp

app = Flask(__name__)

# Configuración BD
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Registrar controladores
app.register_blueprint(auth_bp)
app.register_blueprint(paginas_bp)
app.register_blueprint(consumo_bp)

# Crear la base de datos al inicio
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

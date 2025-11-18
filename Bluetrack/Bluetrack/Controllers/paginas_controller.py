from flask import Blueprint, render_template

paginas_bp = Blueprint('paginas', __name__)

@paginas_bp.route('/categorias')
def categorias():
    return render_template('categoria.html')

@paginas_bp.route('/reportes')
def reportes():
    return render_template('reporte.html')

@paginas_bp.route('/manual')
def manual():
    return render_template('manual.html')

@paginas_bp.route('/procesos')
def procesos():
    return render_template('procesos.html')

@paginas_bp.route('/comunidad')
def comunidad():
    return render_template('comunidad.html')

@paginas_bp.route('/control')
def control():
    return render_template('control.html')

@paginas_bp.route('/calculadora')
def calculadora():
    return render_template('calculadora.html')

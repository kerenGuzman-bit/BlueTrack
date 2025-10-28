from flask import Blueprint, render_template, request
from services.consumo_services import calcular_consumo

consumo_bp = Blueprint('consumo', __name__)

@consumo_bp.route('/consumo', methods=['GET', 'POST'])
def consumo():
    if request.method == 'POST':
        consumo_total = float(request.form['consumo'])
        personas = int(request.form['personas'])
        dias = int(request.form['dias'])
        resultado = calcular_consumo(consumo_total, personas, dias)
        return render_template('resultado.html', resultado=resultado)
    return render_template('consumo.html')

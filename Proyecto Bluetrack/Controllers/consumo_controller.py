from flask import Blueprint, render_template, request
from services.consumo_services import analizar_consumo_promedio

consumo_bp = Blueprint('consumo_bp', __name__)

@consumo_bp.route('/manual', methods=['GET', 'POST'])
def manual_control():
    resultado = None
    error = None

    if request.method == 'POST':
        try:
            # Leer los valores del formulario
            cantidad_agua = float(request.form['cantidad_agua'])
            personas = int(request.form['personas'])
            dias = int(request.form['dias'])

            # Llamar al servicio que hace el cálculo
            resultado = analizar_consumo_promedio(cantidad_agua, personas, dias)

        except Exception as e:
            error = str(e)

    # Renderizar manual.html con los resultados
    return render_template('manual.html', resultado=resultado, error=error)

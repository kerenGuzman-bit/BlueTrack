def calcular_consumo(consumo_total, personas, dias):
    LIMITE = 100
    permitido = personas * LIMITE * dias
    diferencia = consumo_total - permitido
    promedio = consumo_total / (personas * dias)
    estado = "Dentro del límite" if diferencia <= 0 else "Excedido"

    return {
        "consumo_total": consumo_total,
        "permitido": permitido,
        "diferencia": diferencia,
        "promedio": promedio,
        "estado": estado
    }

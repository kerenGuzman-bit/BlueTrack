def analizar_consumo(consumo_actual, promedio):
    """
    Analiza el consumo de agua y devuelve estado, mensaje y tips.
    """
    resultado = {}

    if consumo_actual <= promedio * 1.15:
        resultado["estado"] = "Normal"
        resultado["mensaje"] = "Tu consumo está dentro del rango habitual. ¡Buen trabajo!"
        resultado["tips"] = [
            "Mantén tus hábitos de consumo responsables.",
            "Reutiliza el agua de la lavadora para limpiar pisos o patios."
        ]
    elif consumo_actual <= promedio * 1.3:
        resultado["estado"] = "Alto"
        resultado["mensaje"] = "Tu consumo está ligeramente por encima del promedio."
        resultado["tips"] = [
            "Verifica si hay fugas pequeñas en grifos o sanitarios.",
            "Evita lavar el carro con manguera."
        ]
    else:
        resultado["estado"] = "Excesivo"
        resultado["mensaje"] = "Tu consumo es muy alto. Podrías tener fugas o malos hábitos de uso."
        resultado["tips"] = [
            "Cierra la llave mientras te cepillas o te enjabonas.",
            "Revisa el medidor por fugas ocultas.",
            "Riega las plantas en la noche para reducir evaporación."
        ]

    return resultado


def analizar_consumo_promedio(consumo_litros: float, personas: int, dias: int):
    """
    Analiza el consumo usando litros totales, número de personas y días del período.
    Retorna estado, mensaje, tips y el indicador L/pp/día.
    """
    if personas <= 0 or dias <= 0:
        raise ValueError("Personas y días deben ser mayores que cero.")

    lppd = consumo_litros / (personas * dias)  # litros por persona por día

    # Umbrales de referencia (ajústalos si quieres):
    # Normal:   <= 120 L/pp/día
    # Alto:     121–160 L/pp/día
    # Excesivo: > 160 L/pp/día
    if lppd <= 120:
        estado = "Normal"
        mensaje = f"Consumo saludable: {lppd:.0f} L por persona/día."
        tips = [
            "Mantén los buenos hábitos de ahorro.",
            "Reutiliza agua (lavadora, enjuagues) para limpieza de pisos/patios."
        ]
    elif lppd <= 160:
        estado = "Alto"
        mensaje = f"Consumo por encima del óptimo: {lppd:.0f} L por persona/día."
        tips = [
            "Revisa fugas en sanitarios y grifos (prueba del papel o del medidor).",
            "Evita manguera para lavar; usa balde y gatillo en duchas."
        ]
    else:
        estado = "Excesivo"
        mensaje = f"Consumo muy alto: {lppd:.0f} L por persona/día."
        tips = [
            "Cierra la llave mientras te enjabonas o te cepillas.",
            "Programa revisión del medidor por fugas ocultas.",
            "Riega plantas de noche para reducir evaporación."
        ]

    return {
        "estado": estado,
        "mensaje": mensaje,
        "tips": tips,
        "lppd": lppd
    }

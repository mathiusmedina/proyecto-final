def calcular_co2(distancia, transporte):
    """
    Calcula CO2 en gramos por km según tipo de transporte
    """
    factores = {
        "Auto": 120,
        "Bus": 68,
        "Tren": 41,
        "Bici": 0,
        "Caminar": 0
    }
    return distancia * factores[transporte]


def mejor_transporte(distancia):
    """
    Devuelve la mejor opción según distancia y su explicación
    """
    # Selección lógica realista
    if distancia < 2:
        transporte = "Caminar"
        razon = "La distancia es corta, caminar es saludable y no emite CO₂."
    elif distancia < 10:
        transporte = "Bici"
        razon = "La distancia es adecuada para bicicleta, cero emisiones y rápido."
    elif distancia < 50:
        transporte = "Bus"
        razon = "El transporte público es eficiente para distancias medias, menos emisiones que el coche."
    else:
        transporte = "Tren"
        razon = "Para largas distancias, el tren es más rápido y ecológico que el auto."

    # Calcular ahorro potencial comparando con la peor opción
    transportes = ["Auto", "Bus", "Tren", "Bici", "Caminar"]
    resultados = {t: calcular_co2(distancia, t) for t in transportes}
    peor = max(resultados, key=resultados.get)
    ahorro = resultados[peor] - resultados[transporte]

    return {
        "mejor": transporte,
        "razon": razon,
        "ahorro": ahorro,
        "distancia": distancia,
        "resultados": resultados,
        "peor": peor
    }
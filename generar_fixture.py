def generar_fixture(equipos):
    """
    Genera el fixture de un campeonato todos contra todos 
    con 20 equipos y 19 fechas.
    
    - Cada equipo juega contra todos los demás una sola vez.
    - Se organiza en 19 fechas.
    - Cada partido se guarda como una tupla (equipo_local, equipo_visitante).
    - Devuelve una lista de listas: fixture[fecha] -> lista de partidos.
    """

    # Validación: deben ser 20 equipos
    if len(equipos) != 20:
        print("Error: Se requieren exactamente 20 equipos.")
        return []

    n = len(equipos)
    fixture = []  # Lista que contendrá las 19 fechas

    # Algoritmo round-robin (rotación de equipos)
    for ronda in range(n - 1):  # Se generan 19 fechas
        fecha = []
        for i in range(n // 2):
            equipo_local = equipos[i]
            equipo_visitante = equipos[n - 1 - i]

            # En cada ronda, alternamos quién es local/visitante
            if ronda % 2 == 0:
                fecha.append((equipo_local, equipo_visitante))
            else:
                fecha.append((equipo_visitante, equipo_local))

        fixture.append(fecha)

        # Rotar los equipos (menos el primero que queda fijo)
        equipos = [equipos[0]] + [equipos[-1]] + equipos[1:-1]

    return fixture

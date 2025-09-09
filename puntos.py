def calcular_puntos(fixture, equipos, matriz_goles_a_favor):
    """
    Asigna puntos a cada equipo basándose en los resultados de la simulación.

    Args:
        fixture (list): El calendario de partidos del torneo.
        equipos (list): La lista de equipos participantes.
        matriz_goles_a_favor (list): La matriz con los goles a favor de cada equipo.

    Returns:
        dict: Un diccionario donde la clave es el nombre del equipo y el valor es su puntaje total.
    """
    # Inicializamos un diccionario para guardar los puntos de cada equipo.
    puntos = {equipo: 0 for equipo in equipos}
    
    # Creamos un mapeo de equipos a índices para acceder a la matriz.
    mapeo_equipos = {equipo: i for i, equipo in enumerate(equipos)}
    
    # Recorremos cada fecha y cada partido del fixture.
    for fecha_num, fecha in enumerate(fixture):
        for equipo1, equipo2 in fecha:
            # Obtenemos los índices de los equipos.
            idx1 = mapeo_equipos[equipo1]
            idx2 = mapeo_equipos[equipo2]
            
            # Consultamos los goles de la matriz ya generada.
            goles_equipo1 = matriz_goles_a_favor[idx1][fecha_num]
            goles_equipo2 = matriz_goles_a_favor[idx2][fecha_num]
            
            # Aplicamos la lógica de asignación de puntos.
            if goles_equipo1 > goles_equipo2:
                puntos[equipo1] += 3  # 3 puntos para el ganador.
            elif goles_equipo2 > goles_equipo1:
                puntos[equipo2] += 3  # 3 puntos para el ganador.
            else:
                puntos[equipo1] += 1  # 1 punto para ambos en caso de empate.
                puntos[equipo2] += 1
                
    return puntos


def imprimir_tabla_puntos(puntos_torneo):
    """
    Imprime la tabla de puntos ordenada de mayor a menor puntaje.

    Args:
        puntos_torneo (dict): Diccionario con los puntos de cada equipo.
    """
    print("\n--- TABLA DE POSICIONES ---")
    
    # 1. Convertir el diccionario a una lista de tuplas (equipo, puntaje).
    #    Por ejemplo: [('Equipo A', 6), ('Equipo C', 4), ...]
    lista_puntos = list(puntos_torneo.items())

    # 2. Ordenar la lista.
    #    La función 'sort' ordena la lista en su lugar.
    #    'key=lambda item: item[1]' le dice a Python que ordene basándose en el segundo
    #    elemento de cada tupla (que es el puntaje).
    #    'reverse=True' asegura que el orden sea de mayor a menor.
    lista_puntos.sort(key=lambda item: item[1], reverse=True)

    # 3. Imprimir la lista ordenada.
    for equipo, puntaje in lista_puntos:
        print(f"{equipo:<15} Puntos: {puntaje}")

# Ejemplo de uso
# Suponiendo que 'puntos_torneo' es un diccionario ya calculado, por ejemplo:
# puntos_torneo = {'Equipo A': 6, 'Equipo B': 1, 'Equipo C': 4, 'Equipo D': 1}
# Si llamas a la función con este diccionario:
# imprimir_tabla_posiciones(puntos_torneo)
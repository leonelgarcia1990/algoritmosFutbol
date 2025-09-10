def calcular_puntos(fixture, equipos, matriz_goles_a_favor):

    num_equipos = len(equipos)

    puntos = [0] * num_equipos

    # Recorremos cada fecha del torneo.
    for fecha_num in range(len(fixture)):
        fecha = fixture[fecha_num]

        # Recorremos cada partido en la fecha.
        for partido in fecha:
            equipo1 = partido[0]
            equipo2 = partido[1]

            idx1 = equipos.index(equipo1)
            idx2 = equipos.index(equipo2)

            goles_eq1 = matriz_goles_a_favor[idx1][fecha_num]
            goles_eq2 = matriz_goles_a_favor[idx2][fecha_num]

            if goles_eq1 > goles_eq2:
                puntos[idx1] += 3
            elif goles_eq2 > goles_eq1:
                puntos[idx2] += 3
            else:
                puntos[idx1] += 1
                puntos[idx2] += 1

    return puntos

def imprimir_tabla_ordenada(equipos, puntos):
    
    # Se crea una copia de las listas para ordenarlas sin modificar las originales. Buena practica. 
    equipos_ordenados = list(equipos)
    puntos_ordenados = list(puntos)

    # Algoritmo de ordenamiento de burbuja.
    n = len(puntos_ordenados)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if puntos_ordenados[j] < puntos_ordenados[j+1]:
                # Se intercambian los puntos
                puntos_ordenados[j], puntos_ordenados[j+1] = puntos_ordenados[j+1], puntos_ordenados[j]
                # Se intercambian los equipos de la misma forma para mantener la relación
                equipos_ordenados[j], equipos_ordenados[j+1] = equipos_ordenados[j+1], equipos_ordenados[j]
    
    # Imprimir la tabla de posiciones
    print("\n" + "--- TABLA DE POSICIONES ---".center(40))
    print("-" * 40)
    print(f"{'Pos.':<5} {'Equipo':<20} {'Puntos':>10}")
    print("-" * 40)
    
    for i in range(len(equipos_ordenados)):
        posicion = i + 1
        equipo = equipos_ordenados[i]
        puntos_equipo = puntos_ordenados[i]
        print(f"{posicion:<5} {equipo:<20} {puntos_equipo:>10}")
    print("-" * 40)

    campeon = equipos_ordenados[0]
    print(f"\n¡El CAMPEÓN del torneo es {campeon}!")
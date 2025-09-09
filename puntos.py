def calcular_puntos(fixture, equipos, matriz_goles_a_favor):
    """
    Asigna puntos a cada equipo basándose en los resultados de la simulación.
    """
    # Inicializamos un diccionario para guardar los puntos de cada equipo.
    puntos = {equipo: 0 for equipo in equipos}
    
    # Recorremos cada fecha y cada partido del fixture.
    for fecha_num, fecha in enumerate(fixture):
        for equipo1, equipo2 in fecha:
            # Obtenemos los índices de los equipos.
            # Usamos el método index() para encontrar la posición del equipo.
            idx1 = equipos.index(equipo1)
            idx2 = equipos.index(equipo2)
            
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

#funcion para imprimir tabla de puntos

def imprimir_tabla_puntos(puntos_torneo):
    """
    Imprime la tabla de puntos ordenada de mayor a menor puntaje.

    Args:
        puntos_torneo (dict): Diccionario con los puntos de cada equipo.
    """
    print("\n" + f"{'--- TABLA DE POSICIONES ---':^37}")
    print(f"{'Equipo':^20}  {'Puntos':^6}")

    
   
    lista_puntos = list(puntos_torneo.items())

    # 2. Ordenar la lista.
    #    La función 'sort' ordena la lista en su lugar.
    #    'key=lambda item: item[1]' le dice a Python que ordene basándose en el segundo
    #    elemento de cada tupla (que es el puntaje).
    #    'reverse=True' asegura que el orden sea de mayor a menor.
    lista_puntos.sort(key=lambda item: item[1], reverse=True)

    # 3. Imprimir la lista ordenada.
    for equipo, puntaje in lista_puntos:
        print(f"{equipo[:20]:^20}  {puntaje:^6}")

    
    # Mensaje al campeón (primer lugar de la tabla)
    campeon, puntos = lista_puntos[0]
    
    print("\nFELICITACIONES", campeon.upper(), "!!!")
    print(f"Se consagra campeón con {puntos} puntos.")


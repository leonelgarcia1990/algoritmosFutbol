


def calcular_puntos(fixture, equipos, matriz_goles_a_favor):
    """
    Calcula los puntos, goles a favor y goles en contra de cada equipo
    y los devuelve en una lista de listas.
    """
    num_equipos = len(equipos)
    # Inicializamos la lista principal con listas vacías.
    datos_puntos = [[0, 0, 0] for _ in range(num_equipos)]
    # Formato: [puntos, goles_a_favor, goles_en_contra]

    for fecha_num, fecha in enumerate(fixture):
        for equipo1, equipo2 in fecha:
            idx1 = equipos.index(equipo1)
            idx2 = equipos.index(equipo2)
            
            goles_eq1 = matriz_goles_a_favor[idx1][fecha_num]
            goles_eq2 = matriz_goles_a_favor[idx2][fecha_num]
            
            # Asignación de puntos
            if goles_eq1 > goles_eq2:
                datos_puntos[idx1][0] += 3
            elif goles_eq2 > goles_eq1:
                datos_puntos[idx2][0] += 3
            else:
                datos_puntos[idx1][0] += 1
                datos_puntos[idx2][0] += 1
                
            # Goles a favor y en contra
            datos_puntos[idx1][1] += goles_eq1
            datos_puntos[idx1][2] += goles_eq2
            datos_puntos[idx2][1] += goles_eq2
            datos_puntos[idx2][2] += goles_eq1

    return datos_puntos




def imprimir_tabla(equipos, datos_completos):
    """
    Ordena e imprime la tabla de posiciones.
    """
    n = len(datos_completos)
    
    # Algoritmo de ordenamiento para ordenar la lista de listas.
    # El nombre del equipo (índice 3) se usa para poder imprimirlo.
    for i in range(n - 1):
        for j in range(n - 1 - i):
            # Criterio principal: puntos (índice 0)
            if datos_completos[j][0] < datos_completos[j+1][0]:
                datos_completos[j], datos_completos[j+1] = datos_completos[j+1], datos_completos[j]
            # Criterio de desempate: diferencia de gol (índice 3)
            elif datos_completos[j][0] == datos_completos[j+1][0] and datos_completos[j][3] < datos_completos[j+1][3]:
                datos_completos[j], datos_completos[j+1] = datos_completos[j+1], datos_completos[j]

    # Imprimir la tabla ya ordenada
    print("\n" + f"{'--- TABLA DE POSICIONES ---':^37}")
    print(f"{'Equipo':^20}  {'Puntos':^6}  {'Dif. Gol':^8}")
    
    for i in range(len(equipos)):
        puntos_eq = datos_completos[i][0]
        dif_gol_eq = datos_completos[i][3]
        print(f"{equipos[i][:20]:^20}  {puntos_eq:^6}  {dif_gol_eq:^8}")

    # Mensaje al campeón
    campeon = equipos[0]
    puntos_campeon = datos_completos[0][0]
    dif_gol_campeon = datos_completos[0][3]
    
    print("\n¡FELICITACIONES", campeon.upper(), "!!!")
    print(f"Se consagra campeón con {puntos_campeon} puntos y una diferencia de gol de {dif_gol_campeon}.")
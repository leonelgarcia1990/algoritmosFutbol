
def calcular_puntos(fixture, equipos, matriz_goles_a_favor):
    
   # Calcula solo los puntos de cada equipo y los devuelve en una lista.
    
    num_equipos = len(equipos)

    # Creamos una lista para almacenar los puntos de cada equipo.
    puntos = []
    # Usamos 'i' como una variable simple de conteo.
    for i in range(num_equipos):
        puntos.append(0)

    # Recorremos cada fecha del torneo.
    for fecha_num in range(len(fixture)):
        fecha = fixture[fecha_num]

        # Recorremos cada partido en la fecha.
        for partido in fecha:
            equipo1 = partido[0]
            equipo2 = partido[1]

            # Obtenemos los índices de los equipos.
            idx1 = equipos.index(equipo1)
            idx2 = equipos.index(equipo2)

            # Obtenemos los goles anotados por cada equipo en el partido actual.
            goles_eq1 = matriz_goles_a_favor[idx1][fecha_num]
            goles_eq2 = matriz_goles_a_favor[idx2][fecha_num]

            # Asignamos los puntos basados en el resultado.
            if goles_eq1 > goles_eq2:
                puntos[idx1] += 3  # Victoria: 3 puntos
            elif goles_eq2 > goles_eq1:
                puntos[idx2] += 3  # Victoria: 3 puntos
            else:
                puntos[idx1] += 1  # Empate: 1 punto
                puntos[idx2] += 1  # Empate: 1 punto

    return puntos


def imprimir_tabla_ordenada(equipos, puntos):

    # Paso 1: Combinar equipos y puntos para un ordenamiento más sencillo.
    # Se crea una lista de listas, donde cada sublista es [puntos, nombre_equipo].
    tabla = []
    for i in range(len(equipos)):
        tabla.append([puntos[i], equipos[i]])

    # Paso 2: Ordenar la lista 'tabla'
    # Se usa el algoritmo de ordenamiento de burbuja para ordenar por puntos de mayor a menor.
    n = len(tabla)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if tabla[j][0] < tabla[j+1][0]:
                tabla[j], tabla[j+1] = tabla[j+1], tabla[j]
    
    # Paso 3: Imprimir la tabla de posiciones
    print("\n" + "--- TABLA DE POSICIONES ---".center(40))
    print("-" * 40)
    print(f"{'Pos.':<5} {'Equipo':<20} {'Puntos':>10}")
    print("-" * 40)
    
    # Se recorre la lista ya ordenada y se imprime cada fila de la tabla.
    for i in range(len(tabla)):
        posicion = i + 1
        equipo = tabla[i][1]
        puntos_eq = tabla[i][0]
        print(f"{posicion:<5} {equipo:<20} {puntos_eq:>10}")
    print("-" * 40)
    
    # Paso 4: Imprimir al campeón y su puntuación
    campeon = tabla[0][1]
    puntos_campeon = tabla[0][0]
    
    print("\n¡FELICITACIONES", campeon.upper(), "!!!")
    print(f"Se consagra campeón con {puntos_campeon} puntos.")

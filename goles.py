from random import choices

# Definimos las dimensiones fijas del torneo
NUMERO_EQUIPOS = 20
NUMERO_FECHAS = 19

# Función para simular goles en un partido

def simular_goles():
    """Simula y devuelve un solo valor de goles."""
    valores_goles = [0, 1, 2, 3, 4, 5]
    pesos_goles = [30, 30, 23, 10, 5, 2]
    return choices(valores_goles, pesos_goles)[0]

def inicializar_matriz_resultados():
    """Inicializa una matriz de 20x19 con ceros."""
    matriz = []
    for _ in range(NUMERO_EQUIPOS):
        matriz.append([0] * NUMERO_FECHAS)
    return matriz

def simular_torneo(fixture, equipos):
    """
    Simula todos los partidos del torneo y guarda los goles a favor.

    Args:
        fixture (list): El calendario de partidos del torneo.
        equipos (list): La lista de equipos participantes.

    Returns:
        list: Una matriz con los goles a favor de cada equipo por fecha.
    """
    matriz_goles_a_favor = inicializar_matriz_resultados()

    print("\n--- INICIO DE LA SIMULACIÓN DE PARTIDOS ---")

    for fecha_num, fecha in enumerate(fixture):
        print(f"\n--- FECHA {fecha_num + 1} ---")
        
        for equipo1, equipo2 in fecha:
            goles1 = simular_goles()
            goles2 = simular_goles()

            # Usamos el método index() para obtener el índice de cada equipo
            idx1 = equipos.index(equipo1)
            idx2 = equipos.index(equipo2)

            # Asignamos los goles a la matriz usando los índices
            matriz_goles_a_favor[idx1][fecha_num] = goles1
            matriz_goles_a_favor[idx2][fecha_num] = goles2
            
            print(f"{equipo1} {goles1} - {goles2} {equipo2}")

    print("\n--- FIN DE LA SIMULACIÓN ---")
    
    return matriz_goles_a_favor


def calcular_matriz_goles_en_contra(fixture, equipos, matriz_goles_a_favor):
    """
    Calcula y devuelve la matriz de goles en contra a partir de la matriz de goles a favor.

    Args:
        fixture (list): El calendario de partidos.
        equipos (list): La lista de equipos.
        matriz_goles_a_favor (list): La matriz con los goles a favor.

    Returns:
        list: Una matriz con los goles en contra de cada equipo por fecha.
    """
    # Inicializamos la matriz de goles en contra con ceros.
    matriz_goles_en_contra = inicializar_matriz_resultados()
    
    for fecha_num, fecha in enumerate(fixture):
        for equipo1, equipo2 in fecha:
            # Obtenemos los índices de ambos equipos usando el método .index().
            # Este método recorre la lista `equipos` para encontrar la posición de cada nombre.
            idx1 = equipos.index(equipo1)
            idx2 = equipos.index(equipo2)
            
            # Los goles en contra de un equipo son los goles a favor del rival.
            goles_en_contra_equipo1 = matriz_goles_a_favor[idx2][fecha_num]
            goles_en_contra_equipo2 = matriz_goles_a_favor[idx1][fecha_num]
            
            # Asignamos los valores a la nueva matriz.
            matriz_goles_en_contra[idx1][fecha_num] = goles_en_contra_equipo1
            matriz_goles_en_contra[idx2][fecha_num] = goles_en_contra_equipo2
            
    return matriz_goles_en_contra



def imprimir_matriz(matriz, equipos):
    """
    Imprime una matriz de goles con etiquetas de equipo y fecha para su fácil visualización.
    """
    print("           ", end="")
    for i in range(NUMERO_FECHAS):
        print(f"Fecha{i+1:2d}", end=" ")
    print()
    
    for i in range(NUMERO_EQUIPOS):
        nombre_equipo = equipos[i]
        print(f"{nombre_equipo:10}", end="")
        for j in range(NUMERO_FECHAS):
            print(f"{matriz[i][j]:>6}", end=" ")
        print()



def calcular_diferencia_de_goles(equipos, matriz_goles_a_favor, matriz_goles_en_contra):
    """
    Calcula la diferencia de goles de cada equipo.

    Args:
        equipos (list): La lista de equipos del torneo.
        matriz_goles_a_favor (list): La matriz con los goles a favor.
        matriz_goles_en_contra (list): La matriz con los goles en contra.

    Returns:
        dict: Un diccionario donde la clave es el nombre del equipo y el valor es su diferencia de goles.
    """
    diferencia_goles = {}
    
    # Recorremos la lista de equipos para calcular la diferencia de cada uno.
    for i, equipo in enumerate(equipos):
        # La función sum() suma todos los elementos de la fila (los goles de todas las fechas).
        total_goles_a_favor = sum(matriz_goles_a_favor[i])
        total_goles_en_contra = sum(matriz_goles_en_contra[i])
        
        # Calculamos la diferencia y la guardamos en el diccionario.
        diferencia = total_goles_a_favor - total_goles_en_contra
        diferencia_goles[equipo] = diferencia
        
    return diferencia_goles



def imprimir_resumen_goles(equipos, diferencia_goles):
    """
    Imprime la lista de equipos y su diferencia de goles.
    
    Args:
        equipos (list): La lista de equipos.
        diferencia_goles (dict): Un diccionario con la diferencia de goles de cada equipo.
    """
    print("\n--- RESUMEN DE GOLES POR EQUIPO ---")
    print("-----------------------------------")
    
    # Recorremos la lista de equipos para asegurar un orden consistente.
    for equipo in equipos:
        # Obtenemos la diferencia de goles del diccionario.
        diferencia = diferencia_goles[equipo]
        # Imprimimos el nombre del equipo y su diferencia de goles.
        print(f"{equipo:<15} {diferencia}")
    
    print("-----------------------------------")



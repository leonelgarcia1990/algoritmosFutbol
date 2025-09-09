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


    # Definimos el ancho total del bloque de texto

    ANCHO_TOTAL = 40

    for fecha_num, fecha in enumerate(fixture):
    # Centrar el título de la fecha
        titulo = f"--- FECHA {fecha_num + 1} ---"
        print("\n" + titulo.center(ANCHO_TOTAL))

        for equipo1, equipo2 in fecha:
            goles1 = simular_goles()
            goles2 = simular_goles()

            idx1 = equipos.index(equipo1)
            idx2 = equipos.index(equipo2)

            matriz_goles_a_favor[idx1][fecha_num] = goles1
            matriz_goles_a_favor[idx2][fecha_num] = goles2

            # Formateo alineado: nombres a la izquierda/derecha, goles centrados
            print(f"{equipo1:<15} {goles1:^3} - {goles2:^3} {equipo2:>15}")

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



def imprimir_matriz_favor(matriz, equipos):
    """
    Imprime una matriz de goles a favorcon etiquetas de equipo y fecha para su fácil visualización.
    """
    print("Goles a Favor", end=" ")
    for i in range(NUMERO_FECHAS):
        print(f"Fecha{i+1:2d}", end=" ")
    print()
    
    for i in range(NUMERO_EQUIPOS):
        nombre_equipo = equipos[i]
        print(f"{nombre_equipo:10}", end="")
        for j in range(NUMERO_FECHAS):
            print(f"{matriz[i][j]:>7}", end=" ")
        print()


def imprimir_matriz_contra(matriz, equipos):
    """
    Imprime una matriz de goles en contra con etiquetas de equipo y fecha para su fácil visualización.
    """
    print("Goles Recibidos", end=" ")
    for i in range(NUMERO_FECHAS):
        print(f"Fecha{i+1:2d}", end=" ")
    print()
    
    for i in range(NUMERO_EQUIPOS):
        nombre_equipo = equipos[i]
        print(f"{nombre_equipo:10}", end="")
        for j in range(NUMERO_FECHAS):
            print(f"{matriz[i][j]:>7}", end=" ")
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



def imprimir_resumen_goles(equipos, matriz_goles_a_favor, matriz_goles_en_contra):
    """
    Imprime el resumen de goles por equipo.
    """
    ancho_total = 50 # Definimos el ancho total 
    titulo = f'--- RESUMEN DE GOLES POR EQUIPO ---'
    print("\n" + titulo.center(ancho_total))
    print("--------------------------------------------------")
    print(f"{'Goles Recibidos':<17} {'Equipo':^15} {'Goles a Favor':>15}")
    print("--------------------------------------------------")

    for i in range(len(equipos)):
        equipo = equipos[i]

        # Calculamos goles a favor
        gf_total = 0
        for gol in matriz_goles_a_favor[i]:
            gf_total += gol

        # Calculamos goles en contra
        gc_total = 0
        for gol in matriz_goles_en_contra[i]:
            gc_total += gol

        print(f"{gc_total:<17} {equipo:^15} {gf_total:>15}")
    print("--------------------------------------------------")


def obtener_equipos_mas_goleadores(equipos, matriz_goles_a_favor, top_n=5):
    """
    Obtiene los equipos con más goles a favor.

    Args:
        equipos (list): La lista de equipos del torneo.
        matriz_goles_a_favor (list): La matriz con los goles a favor.
        top_n (int): Número de equipos a incluir en el ranking (default: 5).

    Returns:
        list: Lista de tuplas (equipo, total_goles) ordenada de mayor a menor.
    """
    equipos_goles = []
    
    for i, equipo in enumerate(equipos):
        total_goles = sum(matriz_goles_a_favor[i])
        equipos_goles.append((equipo, total_goles))
    
    # Ordenamos por goles de mayor a menor
    equipos_goles.sort(key=lambda x: x[1], reverse=True)
    
    return equipos_goles[:top_n]


def obtener_equipos_menos_goleados(equipos, matriz_goles_en_contra, top_n=5):
    """
    Obtiene los equipos que recibieron menos goles (mejor defensa).

    Args:
        equipos (list): La lista de equipos del torneo.
        matriz_goles_en_contra (list): La matriz con los goles en contra.
        top_n (int): Número de equipos a incluir en el ranking (default: 5).

    Returns:
        list: Lista de tuplas (equipo, total_goles_recibidos) ordenada de menor a mayor.
    """
    equipos_goles_contra = []
    
    for i, equipo in enumerate(equipos):
        total_goles_contra = sum(matriz_goles_en_contra[i])
        equipos_goles_contra.append((equipo, total_goles_contra))
    
    # Ordenamos por goles recibidos de menor a mayor
    equipos_goles_contra.sort(key=lambda x: x[1])
    
    return equipos_goles_contra[:top_n]


def obtener_equipos_mejor_diferencia(equipos, matriz_goles_a_favor, matriz_goles_en_contra, top_n=5):
    """
    Obtiene los equipos con mejor diferencia de goles.

    Args:
        equipos (list): La lista de equipos del torneo.
        matriz_goles_a_favor (list): La matriz con los goles a favor.
        matriz_goles_en_contra (list): La matriz con los goles en contra.
        top_n (int): Número de equipos a incluir en el ranking (default: 5).

    Returns:
        list: Lista de tuplas (equipo, diferencia_goles) ordenada de mayor a menor.
    """
    equipos_diferencia = []
    
    for i, equipo in enumerate(equipos):
        goles_favor = sum(matriz_goles_a_favor[i])
        goles_contra = sum(matriz_goles_en_contra[i])
        diferencia = goles_favor - goles_contra
        equipos_diferencia.append((equipo, diferencia))
    
    # Ordenamos por diferencia de mayor a menor
    equipos_diferencia.sort(key=lambda x: x[1], reverse=True)
    
    return equipos_diferencia[:top_n]


def imprimir_rankings(equipos, matriz_goles_a_favor, matriz_goles_en_contra):
    """
    Imprime los diferentes rankings de equipos.
    """
    ancho_total = 50
    
    # Ranking de goleadores
    print("\n" + "--- TOP 5 EQUIPOS MÁS GOLEADORES ---".center(ancho_total))
    print("-" * ancho_total)
    top_goleadores = obtener_equipos_mas_goleadores(equipos, matriz_goles_a_favor)
    print(f"{'Pos':<4} {'Equipo':<20} {'Goles':>10}")
    print("-" * ancho_total)
    for i, (equipo, goles) in enumerate(top_goleadores, 1):
        print(f"{i:<4} {equipo:<20} {goles:>10}")
    
    # Ranking de defensas
    print("\n" + "--- TOP 5 MEJORES DEFENSAS ---".center(ancho_total))
    print("-" * ancho_total)
    mejores_defensas = obtener_equipos_menos_goleados(equipos, matriz_goles_en_contra)
    print(f"{'Pos':<4} {'Equipo':<20} {'Goles Rec':>10}")
    print("-" * ancho_total)
    for i, (equipo, goles_contra) in enumerate(mejores_defensas, 1):
        print(f"{i:<4} {equipo:<20} {goles_contra:>10}")
    
    # Ranking de diferencia de goles
    print("\n" + "--- TOP 5 MEJOR DIFERENCIA DE GOLES ---".center(ancho_total))
    print("-" * ancho_total)
    mejor_diferencia = obtener_equipos_mejor_diferencia(equipos, matriz_goles_a_favor, matriz_goles_en_contra)
    print(f"{'Pos':<4} {'Equipo':<20} {'Dif Goles':>10}")
    print("-" * ancho_total)
    for i, (equipo, diferencia) in enumerate(mejor_diferencia, 1):
        signo = "+" if diferencia >= 0 else ""
        print(f"{i:<4} {equipo:<20} {signo}{diferencia:>9}")
    
    print("-" * ancho_total)
from random import choices

# Definimos las dimensiones fijas del torneo
NUMERO_EQUIPOS = 20
NUMERO_FECHAS = 19

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

def generar_fixture(equipos):
    """
    Genera el fixture de un campeonato todos contra todos (round-robin)
    con 20 equipos y 19 fechas, usando listas.
    """
    if len(equipos) != 20:
        print("Error: Se requieren exactamente 20 equipos.")
        return []

    n = len(equipos)
    fixture = []

    for ronda in range(n - 1):
        fecha = []
        for i in range(n // 2):
            equipo_local = equipos[i]
            equipo_visitante = equipos[n - 1 - i]

            if ronda % 2 == 0:
                fecha.append([equipo_local, equipo_visitante])
            else:
                fecha.append([equipo_visitante, equipo_local])

        fixture.append(fecha)
        equipos = [equipos[0]] + [equipos[-1]] + equipos[1:-1]

    return fixture

def simular_torneo(fixture, equipos):
   
    matriz_goles_a_favor = inicializar_matriz_resultados()
    
    print("\n--- INICIO DE LA SIMULACIÓN DE PARTIDOS ---")
    
    for fecha_num in range(NUMERO_FECHAS):
        fecha = fixture[fecha_num]
        print(f"\n--- FECHA {fecha_num + 1} ---")
        for partido in fecha:
            equipo_local = partido[0]
            equipo_visitante = partido[1]
            
            goles1 = simular_goles()
            goles2 = simular_goles()
            
            idx1 = equipos.index(equipo_local)
            idx2 = equipos.index(equipo_visitante)
            
            matriz_goles_a_favor[idx1][fecha_num] = goles1
            matriz_goles_a_favor[idx2][fecha_num] = goles2

            # Se añade la diferencia de gol del partido
            diferencia_gol_partido = goles1 - goles2

            print(f"{equipo_local:<15} {goles1} - {goles2} {equipo_visitante:>15} (Dif: {diferencia_gol_partido:+})")
            
    return matriz_goles_a_favor

def calcular_goles_en_contra(fixture, equipos, matriz_goles_a_favor):
    
   # Calcula y devuelve la matriz de goles en contra basándose en la matriz de goles a favor.
   
    num_equipos = len(equipos)
    num_fechas = len(fixture)
    
    # Se corrige el nombre de la variable para evitar la confusión
    matriz_goles_en_contra = []
    for _ in range(num_equipos):
        fila = []
        for _ in range(num_fechas):
            fila.append(0)
        matriz_goles_en_contra.append(fila)

    for fecha_num in range(num_fechas):
        fecha = fixture[fecha_num]
        for partido in fecha:
            equipo_local = partido[0]
            equipo_visitante = partido[1]
            
            idx1 = equipos.index(equipo_local)
            idx2 = equipos.index(equipo_visitante)
            
            goles1 = matriz_goles_a_favor[idx1][fecha_num]
            goles2 = matriz_goles_a_favor[idx2][fecha_num]
            
            matriz_goles_en_contra[idx1][fecha_num] = goles2
            matriz_goles_en_contra[idx2][fecha_num] = goles1
            
    return matriz_goles_en_contra

def calcular_diferencia_de_goles(equipos, matriz_goles_a_favor, goles_en_contra):
    
    #Calcula la diferencia de goles para cada equipo.
    
    diferencia_goles = []

    for i in range(len(equipos)):
        total_goles_a_favor = sum(matriz_goles_a_favor[i])
        total_goles_en_contra = sum(goles_en_contra[i])
        
        diferencia = total_goles_a_favor - total_goles_en_contra
        diferencia_goles.append(diferencia)
        
    return diferencia_goles

def imprimir_matriz_favor(matriz, equipos):
    
    #Imprime una matriz de goles a favor con etiquetas de equipo y fecha.
    
    print("\n--- GOLES A FAVOR ---")
    print("           ", end="")
    for i in range(NUMERO_FECHAS):
        print(f"Fecha{i+1:2d}", end=" ")
    print()
    
    for i in range(NUMERO_EQUIPOS):
        nombre_equipo = equipos[i]
        print(f"{nombre_equipo:<10}", end="")
        for j in range(NUMERO_FECHAS):
            print(f"{matriz[i][j]:>7}", end=" ")
        print()
    print()

def imprimir_matriz_contra(matriz, equipos):
    
    #Imprime una matriz de goles en contra con etiquetas de equipo y fecha.
    
    print("\n--- GOLES EN CONTRA ---")
    print("           ", end="")
    for i in range(NUMERO_FECHAS):
        print(f"Fecha{i+1:2d}", end=" ")
    print()
    
    for i in range(NUMERO_EQUIPOS):
        nombre_equipo = equipos[i]
        print(f"{nombre_equipo:<10}", end="")
        for j in range(NUMERO_FECHAS):
            print(f"{matriz[i][j]:>7}", end=" ")
        print()
    print()

def imprimir_resumen_goles(equipos, matriz_goles_a_favor, goles_en_contra):
     
    #Imprime el resumen de goles por equipo.
    ancho_total = 50
    titulo = '--- RESUMEN DE GOLES POR EQUIPO ---'
    print("\n" + titulo.center(ancho_total))
    print("-" * ancho_total)
    print(f"{'Equipo':<15} {'Goles Favor':>15} {'Goles Contra':>15} {'Dif. Gol':>12}")
    print("-" * ancho_total)
    
    for i in range(len(equipos)):
        equipo = equipos[i]
        total_a_favor = sum(matriz_goles_a_favor[i])
        total_en_contra = sum(matriz_goles_en_contra[i])
        diferencia_gol = total_a_favor - total_en_contra
        print(f"{equipo:<15} {total_a_favor:>15} {total_en_contra:>15} {diferencia_gol:>12}")
    print("-" * ancho_total)
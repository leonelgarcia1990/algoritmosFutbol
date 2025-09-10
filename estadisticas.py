def obtener_equipos_mas_goleadores(equipos, matriz_goles_a_favor, top_n=5):

  #  Obtiene los equipos con más goles a favor.

    equipos_goles = []
    
    for i, equipo in enumerate(equipos):
        total_goles = sum(matriz_goles_a_favor[i])
        equipos_goles.append((equipo, total_goles))
    
    # Ordenamos por goles de mayor a menor
    equipos_goles.sort(key=lambda x: x[1], reverse=True)
    
    return equipos_goles[:top_n]


def obtener_equipos_menos_goleados(equipos, matriz_goles_en_contra, top_n=5):
    
   # Obtiene los equipos que recibieron menos goles (mejor defensa).

    equipos_goles_contra = []
    
    for i, equipo in enumerate(equipos):
        total_goles_contra = sum(matriz_goles_en_contra[i])
        equipos_goles_contra.append((equipo, total_goles_contra))
    
    # Ordenamos por goles recibidos de menor a mayor
    equipos_goles_contra.sort(key=lambda x: x[1])
    
    return equipos_goles_contra[:top_n]


def obtener_equipos_mejor_diferencia(equipos, matriz_goles_a_favor, matriz_goles_en_contra, top_n=5):

   # Obtiene los equipos con mejor diferencia de goles.

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

   # Imprime los diferentes rankings de equipos.

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

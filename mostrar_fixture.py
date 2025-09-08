def mostrar_fixture(fixture):
    print("\n=== FIXTURE DEL CAMPEONATO ===")
    
    for i in range(len(fixture)):  # i es el índice de la fecha
        print(f"\nFecha {i+1}:")
        partidos = fixture[i]
        for j in range(len(partidos)):  # j es el índice del partido en la fecha
            local, visitante = partidos[j]
            print(f"{local} vs {visitante}")

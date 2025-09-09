
def generar_fixture(equipos):
   
    n = len(equipos)
    fixture = []

    for ronda in range(n - 1):
        fecha = []
        for i in range(n // 2):
            #creacion de dos listas una para local y visitante
            equipo_local = equipos[i]
            equipo_visitante = equipos[n - 1 - i]
            
            #local y visitante alternado las fechas    
            if ronda % 2 == 0:
                fecha.append([equipo_local, equipo_visitante])
            else:
                fecha.append([equipo_visitante, equipo_local])

        fixture.append(fecha)

        #creacion de una nueva lista rontando los equipos para que no se repitan las fechas. 
        equipos = [equipos[0]] + [equipos[-1]] + equipos[1:-1]

    return fixture
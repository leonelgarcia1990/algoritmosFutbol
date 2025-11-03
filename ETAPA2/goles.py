import random

def verificar_goles_simulados(fixture):
    if not fixture:
        return False
    
    for fecha in fixture:
        partidos = fixture[fecha]
        if len(partidos) > 0:
            if 'goles_local' in partidos[0]:
                return True
    
    return False


def calcular_tabla(fixture):
    tabla = {}
    
    for fecha in fixture:
        partidos = fixture[fecha]
        for partido in partidos:
            local = partido['local']
            visitante = partido['visitante']
            goles_local = partido['goles_local']
            goles_visitante = partido['goles_visitante']
            
            if local not in tabla:
                tabla[local] = {'puntos': 0, 'gf': 0, 'gc': 0, 'diferencia': 0}
            if visitante not in tabla:
                tabla[visitante] = {'puntos': 0, 'gf': 0, 'gc': 0, 'diferencia': 0}
            
            tabla[local]['gf'] = tabla[local]['gf'] + goles_local
            tabla[local]['gc'] = tabla[local]['gc'] + goles_visitante
            tabla[visitante]['gf'] = tabla[visitante]['gf'] + goles_visitante
            tabla[visitante]['gc'] = tabla[visitante]['gc'] + goles_local
            
            if goles_local > goles_visitante:
                tabla[local]['puntos'] = tabla[local]['puntos'] + 3
            elif goles_local < goles_visitante:
                tabla[visitante]['puntos'] = tabla[visitante]['puntos'] + 3
            else:
                tabla[local]['puntos'] = tabla[local]['puntos'] + 1
                tabla[visitante]['puntos'] = tabla[visitante]['puntos'] + 1
    
    for equipo in tabla:
        tabla[equipo]['diferencia'] = tabla[equipo]['gf'] - tabla[equipo]['gc']
    
    return tabla


def simular_goles(fixture):
    if not fixture:
        print('No hay fixture generado. Por favor, genera el fixture primero.')
        return fixture
    
    print('\n--- Simulando goles para todos los partidos ---\n')
    
    for fecha in fixture:
        partidos = fixture[fecha]
        for partido in partidos:
            goles_local = random.randint(0, 5)
            goles_visitante = random.randint(0, 5)
            
            partido['goles_local'] = goles_local
            partido['goles_visitante'] = goles_visitante
    
    print('Goles simulados exitosamente para todos los partidos!')
    return fixture


def mostrar_resultados(fixture):
    print('\n=== RESULTADOS DEL TORNEO ===\n')
    
    fecha_num = 1
    for fecha in fixture:
        print(f'--- Fecha {fecha_num} ---')
        partidos = fixture[fecha]
        
        for partido in partidos:
            goles_local = partido['goles_local']
            goles_visitante = partido['goles_visitante']
            local = partido['local']
            visitante = partido['visitante']
            
            print(f'{local} {goles_local} - {goles_visitante} {visitante}')
        
        print()
        fecha_num = fecha_num + 1


def calcular_tabla_posiciones(fixture):
    tabla = calcular_tabla(fixture)
    
    lista_tabla = []
    for equipo in tabla:
        lista_tabla.append((equipo, tabla[equipo]))
    
    lista_tabla.sort(key=lambda x: (x[1]['puntos'], x[1]['diferencia']), reverse=True)
    
    print('\n=== TABLA DE POSICIONES ===\n')
    print('Pos  Equipo                      Pts   GF   GC   Dif')
    print('=' * 60)
    
    posicion = 1
    for equipo_data in lista_tabla:
        equipo = equipo_data[0]
        stats = equipo_data[1]
        
        nombre_formato = equipo
        if len(nombre_formato) > 25:
            nombre_formato = nombre_formato[0:25]
        else:
            while len(nombre_formato) < 25:
                nombre_formato = nombre_formato + ' '
        
        print(f'{posicion:2}   {nombre_formato}  {stats["puntos"]:3}   {stats["gf"]:3}  {stats["gc"]:3}  {stats["diferencia"]:+4}')
        posicion = posicion + 1
    
    print()
    
    campeon = lista_tabla[0][0]
    print(f'Equipo Campeon: {campeon}\n')

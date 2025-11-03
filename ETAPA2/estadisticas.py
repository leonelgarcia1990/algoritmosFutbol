from goles import calcular_tabla

def mostrar_estadisticas(fixture):
    print('\n--- Generando estadisticas ---\n')
    
    tabla = calcular_tabla(fixture)
    
    max_gf = max(tabla[equipo]['gf'] for equipo in tabla)
    equipo_mas_gf = ''
    for equipo in tabla:
        if tabla[equipo]['gf'] == max_gf:
            equipo_mas_gf = equipo
            break
    
    min_gc = min(tabla[equipo]['gc'] for equipo in tabla)
    equipo_menos_gc = ''
    for equipo in tabla:
        if tabla[equipo]['gc'] == min_gc:
            equipo_menos_gc = equipo
            break
    
    max_diff = max(tabla[equipo]['diferencia'] for equipo in tabla)
    equipo_mejor_diff = ''
    for equipo in tabla:
        if tabla[equipo]['diferencia'] == max_diff:
            equipo_mejor_diff = equipo
            break
    
    max_goles_totales = 0
    max_goles_equipo = 0
    
    for fecha in fixture:
        partidos = fixture[fecha]
        for partido in partidos:
            goles_local = partido['goles_local']
            goles_visitante = partido['goles_visitante']
            total_goles = goles_local + goles_visitante
            
            max_goles_totales = max(max_goles_totales, total_goles)
            max_goles_equipo = max(max_goles_equipo, goles_local, goles_visitante)
    
    goles_por_fecha = {}
    for fecha in fixture:
        partidos = fixture[fecha]
        goles_por_fecha[fecha] = sum(partido['goles_local'] + partido['goles_visitante'] for partido in partidos)
    
    print('\n--- Generando archivo estadisticas.csv ---\n')
    
    try:
        f = open('estadisticas.csv', 'wt')
        
        f.write('ESTADISTICAS GENERALES\n')
        f.write('Estadistica,Valor\n')
        f.write(f'Equipo con mas goles a favor,{equipo_mas_gf}\n')
        f.write(f'Cantidad de goles a favor,{max_gf}\n')
        f.write(f'Equipo con menos goles en contra,{equipo_menos_gc}\n')
        f.write(f'Cantidad de goles en contra,{min_gc}\n')
        f.write(f'Equipo con mejor diferencia de gol,{equipo_mejor_diff}\n')
        f.write(f'Diferencia de gol,{max_diff}\n')
        f.write(f'Partido con mas goles totales,{max_goles_totales}\n')
        f.write(f'Maximo de goles de un equipo,{max_goles_equipo}\n')
        f.write('\n')
        print('- Equipo con mas goles a favor')
        print('- Equipo con menos goles en contra')
        print('- Equipo con mejor diferencia de gol')
        print('- Partido con mas goles totales')
        print('- Maximo de goles de un equipo')
        
        f.write('GOLES POR EQUIPO\n')
        f.write('Equipo,Goles_Favor\n')
        for equipo in tabla:
            f.write(f'{equipo},{tabla[equipo]["gf"]}\n')
        f.write('\n')
        print('- Goles por Equipo')
        
        f.write('GOLES POR FECHA\n')
        f.write('Fecha,Total_Goles\n')
        for fecha in goles_por_fecha:
            f.write(f'{fecha},{goles_por_fecha[fecha]}\n')
        f.write('\n')
        print('- Goles por Fecha')
        
        f.close()
        print('\nArchivo estadisticas.csv generado correctamente y listo para usar en Excel.\n')
        
    except IOError:
        print('Error al generar estadisticas.csv')



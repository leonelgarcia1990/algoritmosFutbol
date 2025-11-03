def cargar_equipos_para_fixture():
    equipos = []
    try:
        f = open('equipos_manuales.csv', 'rt')
        for linea in f:
            nombre = linea.strip()
            if nombre:
                equipos.append(nombre)
        f.close()
    except IOError:
        print('Error: No se pudo abrir el archivo de equipos.')
    return equipos


def generar_fixture():
    equipos = cargar_equipos_para_fixture()
    
    if len(equipos) != 20:
        print('\nDebe cargar los 20 equipos primero (opcion 2).')
        return None
    
    print(f'\n=== Fixture del Torneo ===')
    
    # Diccionario para almacenar todas las fechas
    fixture = {}
    
    # Generar 19 fechas usando algoritmo round-robin
    for fecha in range(1, 20):
        fixture[fecha] = []
        print(f'--- Fecha {fecha} ---')
        
        # Generar 10 partidos por fecha
        for i in range(10):
            equipo1 = equipos[i]
            equipo2 = equipos[19 - i]
            
            # Alternar local/visitante segun la fecha
            if fecha % 2 == 0:
                equipo1, equipo2 = equipo2, equipo1
            
            # Guardar el partido en el diccionario
            fixture[fecha].append({'local': equipo1, 'visitante': equipo2})
            
            # Imprimir el partido
            print(f'{equipo1} vs {equipo2}')
        
        print()
        
        # Rotar equipos (mantener el primero fijo, rotar los demas)
        equipos = [equipos[0]] + [equipos[-1]] + equipos[1:-1]
    
    print('Fixture generado correctamente con 19 fechas.\n')
    return fixture

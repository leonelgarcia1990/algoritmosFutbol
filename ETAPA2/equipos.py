def cargar_equipo_manual():
    equipos = []
    print('\nIngrese los nombres de los 20 equipos:')
    for i in range(20):
        while True:
            nombre = input(f'Equipo {i+1}: ')
            if not nombre.strip():
                print('El nombre no puede estar vacio. Intente nuevamente.')
            elif len(nombre) > 30:
                print('El nombre no puede superar los 30 caracteres. Intente nuevamente.')
            elif nombre.strip() in equipos:
                print('Este equipo ya fue ingresado. Intente nuevamente.')
            else:
                break
            
        equipos.append(nombre)
    
    print('\nSe completo la carga de los 20 equipos correctamente.')
    guardar_equipos(equipos)
    return equipos


def cargar_equipos_simulados():
    equipos = []
    try:
        f = open('equipos_simulados.csv', 'rt')
        for linea in f:
            nombre = linea.strip()
            if nombre:
                equipos.append(nombre)
        f.close()
        
        if len(equipos) != 20:
            print(f'\nError: Se necesitan exactamente 20 equipos.')
            print(f'El archivo contiene {len(equipos)} equipos.')
            return []
        
        print(f'\nSe cargaron {len(equipos)} equipos desde el archivo simulado correctamente.')
        guardar_equipos(equipos)
        return equipos
        
    except IOError:
        print('Error leyendo archivo de equipos simulados.')
        return []


def guardar_equipos(equipos):
    try:
        f = open('equipos_manuales.csv', 'wt')
        for i in range(20):
            nombre_formateado = equipos[i].strip()
            if i < 19:
                f.write(f"{nombre_formateado}\n")
            else:
                f.write(nombre_formateado)
        f.close()
    except IOError:
        print('Error guardando equipos.')


def cargar_equipos():
    equipos = []
    try:
        f = open('equipos_manuales.csv', 'rt')
        for linea in f:
            nombre = linea.strip()
            if nombre:
                equipos.append(nombre)
        f.close()
    except IOError:
        print('Error: No se pudo cargar el archivo de equipos.')
    return equipos


def listar_equipos(equipos):
    if not equipos:
        print('\nNo hay equipos manuales cargados. Mostrando equipos simulados:')
        try:
            f = open('equipos_simulados.csv', 'rt')
            equipos_simulados = []
            for linea in f:
                nombre = linea.strip()
                if nombre:
                    equipos_simulados.append(nombre)
            f.close()
            
            i = 1
            for nombre in equipos_simulados:
                print(f"{i}. {nombre}")
                i = i + 1
            print(f"\nTotal: {len(equipos_simulados)} equipos simulados.")
        except IOError:
            print('Error al abrir el archivo de equipos simulados.')
        return
    
    print('\nEquipos cargados:')
    i = 1
    for nombre in equipos:
        print(f"{i}. {nombre}")
        i = i + 1
    print(f"\nTotal: {len(equipos)} equipos.")


def menu_equipos():
    while True:
        equipos = cargar_equipos()
        print('\n--- Menu Equipos ---')
        print('1 - Cargar equipos manual')
        print('2 - Cargar equipos simulados (demo rapida)')
        print('3 - Listar equipos')
        print('4 - Volver')
        try:
            opcion = int(input('Elija opcion: ').strip())
            if opcion == 1:
                equipos = cargar_equipo_manual()
            elif opcion == 2:
                equipos = cargar_equipos_simulados()
            elif opcion == 3:
                listar_equipos(equipos)
            elif opcion == 4:
                break
            else:
                raise ValueError
        except ValueError:
            print('Opcion invalida.')
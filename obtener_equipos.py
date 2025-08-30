def obtener_equipos():

    equipos = []
    print("Ingrese los nombres de 20 equipos de Campeonato:")

    i = 0
    while i < 20:
        nombre_equipo = input(f"Equipo {i+1}: ")
        
        # Validacion: no se permiten nombres vacios

        if nombre_equipo.strip() == "":
            print("El nombre no puede estar vacío. Intente nuevamente.")
        

        # Validacion: verifica si el equipo ya fue ingresado
        elif nombre_equipo in equipos:
            print("Este equipo ya fue ingresado. Ingrese otro nombre.")
        else:
            # agrega nombre a la lista y avanza al siguiente equipo
            equipos.append(nombre_equipo)
            i += 1

    print("\n¡Lista de equipos completada!")
    return equipos
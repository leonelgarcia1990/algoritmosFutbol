def validar_y_agregar_equipo(equipos, nombre):
    if len(nombre.strip()) == 0:
        print("¡Error! El nombre del equipo no puede estar vacío. Intenta de nuevo.")
        return False

    nombre_normalizado = " ".join(nombre.strip().split())
    caracteres_permitidos = "áéíóúüñÁÉÍÓÚÜÑ.-'"
    
    for char in nombre_normalizado:
        if (char.isalpha() == False) and (char in caracteres_permitidos == False) and (char.isspace() == False):
            print(f" ¡Error! El nombre contiene caracteres no permitidos: '{char}'. Intenta de nuevo.")
            return False

    nombre_formateado = nombre_normalizado.title()

    if nombre_formateado in equipos:
        print("¡Error! Este equipo ya fue ingresado. Intenta con otro nombre.")
        return False
    
    equipos.append(nombre_formateado)
    print(f"¡Correcto! El equipo '{nombre_formateado}' fue agregado.")
    return True


def obtener_equipos():
    equipos = []
    
    print("\n--- Ingreso de Nombres de Clubes ---")
    print("Por favor, ingresa los nombres de los 20 equipos.")
    print("-" * 40)
    
    i = 0
    while i < 20:
        nombre_ingresado = input(f"Ingresa el nombre del equipo {i + 1}: ")
        
        validado = validar_y_agregar_equipo(equipos, nombre_ingresado)
        
        if validado:
            i += 1
    
    return equipos


def listar_equipos(equipos):
    print("\nLista de equipos:")
    for i in range(len(equipos)):
        print(f"{i+1}. {equipos[i]}")


def matriz_goles(equipos):

    from random import randint

    from random import choices
    # choices(): Puede seleccionar múltiples elementos, con probabilidades personalizadas
    # Definir distribución de probabilidad para los goles con choices
    # Valores posibles: 0, 1, 2, 3, 4, 5
    # Pesos (probabilidades): menor para 0, 4 y 5; mayor para 1, 2 y 3
    valores_goles = [0, 1, 2, 3, 4, 5]
    pesos_goles = [10, 35, 25, 20, 5, 5]  # Total: 100%



    # Crear matriz inicializada con ceros (20 equipos x 19 fechas)
    matriz_goles = []
    for i in range(20):
        # Crear una fila de 19 ceros
        fila_goles = [0] * 19
        matriz_goles.append(fila_goles)



    # Ahora asignamos los goles según la distribución de probabilidad
    for i in range(20):
        for j in range(19):
            # Generar goles según la distribución de probabilidad
            matriz_goles[i][j] = choices(valores_goles, pesos_goles)[0]

    return matriz_goles


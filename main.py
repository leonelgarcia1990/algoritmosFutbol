

# ********************************** IMPORT FUNCIONES PYTHON********************

# ********************************** IMPORT FUNCIONES PROPIAS ******************

from ingreso_equipos import obtener_equipos
from ingreso_equipos import listar_equipos

from generar_fixture import generar_fixture

from goles import simular_torneo
from goles import calcular_matriz_goles_en_contra
from goles import calcular_diferencia_de_goles
from goles import imprimir_matriz_favor
from goles import imprimir_matriz_contra
from goles import imprimir_resumen_goles

from puntos import calcular_puntos
from puntos import imprimir_tabla_puntos



# ***************************** FUNCION MAIN ***********************************
def main():
    
    print("==========================================")
    print("SISTEMA DE GESTIÓN DE EQUIPOS DE FÚTBOL")
    print("==========================================")
    
    # Obtener la lista de equipos
    lista_equipos = obtener_equipos()
    
    # Mostrar la lista de equipos
    listar_equipos(lista_equipos)
    
    #generacion de fixture y print
    fixture = generar_fixture(lista_equipos)

    
    goles_a_favor = simular_torneo(fixture, lista_equipos)
    
    goles_en_contra = calcular_matriz_goles_en_contra(fixture,lista_equipos,goles_a_favor)
    
    #solo para ver como se genera la matriz
    imprimir_matriz_favor(goles_a_favor, lista_equipos)
        
    #solo para ver como se genera la matriz
    imprimir_matriz_contra(goles_en_contra, lista_equipos)
    
    diferencia_total = calcular_diferencia_de_goles(lista_equipos, goles_a_favor, goles_en_contra)

    #solo para ver como se genera la lista
    imprimir_resumen_goles(lista_equipos, matriz_goles_a_favor=goles_a_favor, matriz_goles_en_contra=goles_en_contra)
    
    puntos_torneo = calcular_puntos(fixture, lista_equipos, goles_a_favor)
    
    #solo para ver como se genera la lista
    imprimir_tabla_puntos(puntos_torneo)
    
    
  
# **************************** LLAMADO A FUNCION MAIN **************************

main()




# ********************************** IMPORT FUNCIONES PROPIAS ******************

from ingreso_equipos import obtener_equipos, listar_equipos
from generar_fixture import generar_fixture
from goles import simular_torneo, calcular_goles_en_contra, imprimir_resumen_goles
from puntos import imprimir_tabla_ordenada,calcular_puntos

# ***************************** FUNCION MAIN ***********************************
def main():
    
    print("==========================================")
    print("SISTEMA DE GESTIÓN DE EQUIPOS DE FÚTBOL")
    print("==========================================")
    
    lista_equipos = obtener_equipos()
    
    listar_equipos(lista_equipos)
    
    fixture = generar_fixture(lista_equipos)

    goles_a_favor = simular_torneo(fixture, lista_equipos)
    
    goles_en_contra = calcular_goles_en_contra(fixture, lista_equipos, goles_a_favor)
 
    imprimir_resumen_goles(lista_equipos, goles_a_favor, goles_en_contra)
    
    puntos = calcular_puntos(fixture, lista_equipos, goles_a_favor)

    imprimir_tabla_ordenada(lista_equipos, puntos)

  
# **************************** LLAMADA A LA FUNCION MAIN ***********************
if __name__ == "__main__":
    main()
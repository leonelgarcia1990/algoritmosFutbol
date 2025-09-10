

# ********************************** IMPORT FUNCIONES PYTHON********************

# ********************************** IMPORT FUNCIONES PROPIAS ******************

# Asumimos que estos módulos existen y funcionan correctamente
from ingreso_equipos import obtener_equipos, listar_equipos
from generar_fixture import generar_fixture
from goles import simular_torneo, calcular_goles_en_contra, imprimir_resumen_goles



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
    
    
    goles_en_contra = calcular_goles_en_contra(fixture, lista_equipos, goles_a_favor)
 
    #solo para ver como se genera la lista
    imprimir_resumen_goles(lista_equipos, goles_a_favor,goles_en_contra)

 

  
# **************************** LLAMADO A FUNCION MAIN **************************



main()



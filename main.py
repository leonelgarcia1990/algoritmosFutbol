

# ********************************** IMPORT FUNCIONES PYTHON********************

from random import randint

# ********************************** IMPORT FUNCIONES PROPIAS ******************

from obtener_equipos import obtener_equipos
from mostrar_equipos import mostrar_equipos
from matriz_goles import matriz_goles
# ***************************** VARIABLES GLOBALES *****************************
CANTIDAD_EQUIPOS = 20
goles = []
# ***************************** FUNCION MAIN ***********************************
def main():
    print("SISTEMA DE GESTIÓN DE EQUIPOS DE FÚTBOL")
    print("======================================")
    
    # Obtener la lista de equipos
    equipos = obtener_equipos()
    
    # Mostrar la lista de equipos
    mostrar_equipos(equipos)
   
   #test - muesto en pantalla goles sin formato 
    goles = matriz_goles(equipos)
    print(goles)
    
# **************************** LLAMADO A FUNCION MAIN **************************

main()



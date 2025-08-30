

# ********************************** IMPORT FUNCIONES PYTHON********************

from random import randint

# ********************************** IMPORT FUNCIONES PROPIAS ******************

from obtener_equipos import obtener_equipos
from mostrar_equipos import mostrar_equipos

# ***************************** VARIABLES GLOBALES *****************************
CANTIDAD_EQUIPOS = 20

# ***************************** FUNCION MAIN ***********************************
def main():
 print("SISTEMA DE GESTIÓN DE EQUIPOS DE FÚTBOL")
 print("======================================")
 
 # Obtener la lista de equipos
 equipos = obtener_equipos()
 
 # Mostrar la lista de equipos
 mostrar_equipos(equipos)
 

# **************************** LLAMADO A FUNCION MAIN **************************

main()



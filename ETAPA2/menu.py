from users import usuarios_abm_menu
from equipos import menu_equipos
from fixture import generar_fixture
from goles import simular_goles, mostrar_resultados, calcular_tabla_posiciones, verificar_goles_simulados
from estadisticas import mostrar_estadisticas
from logger import registrar_accion

fixture_global = None

def menu_principal(users):
    global fixture_global
    
    while True:
        print('\n=== Menu Principal ===')
        print('1 - Usuarios ABM')
        print('2 - Equipos')
        print('3 - Generar fixture')
        print('4 - Simular goles')
        print('5 - Ver resultados')
        print('6 - Ver tabla de posiciones')
        print('7 - Ver estadisticas y exportar CSV')
        print('8 - Salir')
        try:
            opcion = int(input('Elija opcion: ').strip())
            if opcion == 1:
                registrar_accion('Ingreso al menu de Usuarios ABM')
                usuarios_abm_menu(users)
            elif opcion == 2:
                registrar_accion('Ingreso al menu de Equipos')
                menu_equipos()
            elif opcion == 3:
                registrar_accion('Intento generar fixture')
                fixture_global = generar_fixture()
                if fixture_global:
                    registrar_accion('Fixture generado exitosamente')
            elif opcion == 4:
                registrar_accion('Intento simular goles')
                if fixture_global is None:
                    registrar_accion('Error: No hay fixture generado')
                    print('\nDebe generar el fixture primero (opcion 3).')
                else:
                    fixture_global = simular_goles(fixture_global)
                    registrar_accion('Goles simulados exitosamente')
            elif opcion == 5:
                registrar_accion('Intento ver resultados')
                if fixture_global is None:
                    registrar_accion('Error: No hay fixture generado')
                    print('\nDebe generar el fixture primero (opcion 3).')
                elif not verificar_goles_simulados(fixture_global):
                    registrar_accion('Error: No hay goles simulados')
                    print('\nDebe simular los goles primero (opcion 4).')
                else:
                    mostrar_resultados(fixture_global)
                    registrar_accion('Resultados mostrados correctamente')
            elif opcion == 6:
                registrar_accion('Intento ver tabla de posiciones')
                if fixture_global is None:
                    registrar_accion('Error: No hay fixture generado')
                    print('\nDebe generar el fixture primero (opcion 3).')
                elif not verificar_goles_simulados(fixture_global):
                    registrar_accion('Error: No hay goles simulados')
                    print('\nDebe simular los goles primero (opcion 4).')
                else:
                    calcular_tabla_posiciones(fixture_global)
                    registrar_accion('Tabla de posiciones mostrada correctamente')
            elif opcion == 7:
                registrar_accion('Intento ver estadisticas y exportar CSV')
                if fixture_global is None:
                    registrar_accion('Error: No hay fixture generado')
                    print('\nDebe generar el fixture primero (opcion 3).')
                elif not verificar_goles_simulados(fixture_global):
                    registrar_accion('Error: No hay goles simulados')
                    print('\nDebe simular los goles primero (opcion 4).')
                else:
                    mostrar_estadisticas(fixture_global)
                    registrar_accion('Estadisticas exportadas correctamente')
            elif opcion == 8:
                registrar_accion('Usuario salio del sistema')
                print('Saliendo del sistema...')
                try:
                    f = open('equipos_manuales.csv', 'wt')
                    f.close()
                except IOError:
                    print('Error: No se pudo limpiar el archivo de equipos.')
                break
            else:
                raise ValueError
        except ValueError:
            registrar_accion('Opcion invalida ingresada')
            print('Opcion invalida.')
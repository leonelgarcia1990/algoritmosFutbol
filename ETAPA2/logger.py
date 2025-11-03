def registrar_accion(accion):
    try:
        f = open('registro.txt', 'at')
        f.write(f'{accion}\n')
        f.close()
    except IOError:
        print('Error: No se pudo registrar la accion en el log.')

def load_users():
    users = {}
    try:
        f = open("users.csv", 'rt')
        for linea in f:
            usuario, password = linea.strip().split(',')
            users[usuario] = {'password': password}
        f.close()
    except IOError:
        print("Error leyendo archivo de usuarios")
    return users


def save_users(users):
    try:
        f = open("users.csv", 'wt')
        users_list = list(users.items())
        for i, (username, data) in enumerate(users_list):
            password = data.get('password', '')
            if i < len(users_list) - 1:
                f.write(f"{username},{password}\n")
            else:
                f.write(f"{username},{password}")
        f.close()
    except IOError:
        print("Error guardando usuarios")


def alta_usuario(users):
    username = input('Nombre de usuario: ').strip().lower()
    if not username:
        print('Nombre de usuario vacio. Operacion cancelada.')
        return
    if username in users:
        print('El usuario ya existe.')
        return
    password = input('Contrasena: ').strip()
    users[username] = {'password': password}
    print(f"Usuario '{username}' creado.")


def baja_usuario(users):
    username = input('Usuario a eliminar (username): ').strip().lower()
    if username not in users:
        print('Usuario no encontrado.')
        return
    if username == 'admin':
        print('El usuario admin no puede ser eliminado.')
        return
    confirm = input(f"Confirma eliminacion de '{username}'? (s para confirmar, cualquier otra tecla para cancelar): ").strip().lower()
    if confirm == 's':
        del users[username]
        print(f"Usuario '{username}' eliminado.")
    else:
        print('Operacion cancelada.')


def modificar_usuario(users):
    username = input('Usuario a modificar (username): ').strip().lower()
    if username not in users:
        print('Usuario no encontrado.')
        return
    print('Dejar campo vacio para no cambiarlo.')
    new_password = input('Nueva contrasena: ').strip()
    if new_password:
        users[username]['password'] = new_password
        print('Contrasena actualizada.')
    else:
        print('No se realizaron cambios.')


def listar_usuarios(users):
    if not users:
        print('No hay usuarios.')
        return
    print('\nUsuarios:')
    for u in users:
        print(f" - {u}")


def usuarios_abm_menu(users):
    while True:
        print('\n--- Usuarios ABM ---')
        print('1 - Alta')
        print('2 - Baja')
        print('3 - Modificar Contrasena')
        print('4 - Listar')
        print('5 - Volver')
        try:
            opcion = int(input('Elija opcion: ').strip())
            if opcion == 1:
                alta_usuario(users)
                save_users(users)
            elif opcion == 2:
                baja_usuario(users)
                save_users(users)
            elif opcion == 3:
                modificar_usuario(users)
                save_users(users)
            elif opcion == 4:
                listar_usuarios(users)
                continue
            elif opcion == 5:
                break
            else:
                raise ValueError
        except ValueError:
            print('Opcion invalida.')
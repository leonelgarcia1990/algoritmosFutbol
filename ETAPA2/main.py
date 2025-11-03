
from menu import menu_principal
from users import load_users
from auth import login
from logger import registrar_accion

def main():
    registrar_accion('=== Sistema iniciado ===')
    users = load_users()
    print('\n=== Login ===')
    usuario = login(users)
    if usuario:
        registrar_accion(f'Login exitoso - Usuario: {usuario}')
        menu_principal(users)
    else:
        registrar_accion('Login fallido - Demasiados intentos')

if __name__ == '__main__':
    main()
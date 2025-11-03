def login(users):
    for _ in range(3):
        username = input('Usuario: ').strip().lower()
        password = input('Contrasena: ').strip()
        
        if username in users and users[username]['password'] == password:
            print(f'\nBienvenido {username}!')
            return username
        
        print('Usuario o contrasena incorrectos.')
    
    print('\nDemasiados intentos fallidos.')
    return None
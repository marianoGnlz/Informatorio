contrasenia = 'ola'

print('Ingrese su contraseña: ', end='')
contraseniaIngresada = input()

if contrasenia != contraseniaIngresada:

    for intentos in range(4):
        
        print('Contraseña incorrecta, intente de nuevo...')
        print('Ingrese su contraseña: ', end='')
        contraseniaIngresada = input()

        if contrasenia == contraseniaIngresada:
            print('Ingreso satisfactorio.')
            break
        
        if intentos == 3:
            print('Cuenta bloqueada.')
else:
    print('Ingreso satisfactorio.')

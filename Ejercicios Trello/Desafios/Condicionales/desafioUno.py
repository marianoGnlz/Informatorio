import os
clear = lambda: os.system('cls')

while True:
    try:
        aniosUtilizandoInsecticida = int(input('¿Cuántos años lleva utilizando insectizidas? - '))
        if (aniosUtilizandoInsecticida >= 10):
            print('Por favor solicite revisión de suelos en su plantación.')
        else:
            print('Intentaremos ayudarte con un nuevo sistema de control de plagas, y cuidaremos el suelo de su plantación.')
        break
    except ValueError:
        print('Ingresó un dato erroneo, intentelo de nuevo...')
        input('Presione enter para continuar...')
        clear()
import os
clear = lambda: os.system('cls')

class bcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'

while True:
    try:
        clear()
        m = abs(int(input('Ingrese la cantidad de filas deseadas: ')))
        break
    except ValueError:
        input('No se puede obtener el valor deseado, intentelo de nuevo...')

while True:
    try:
        clear()
        n = abs(int(input('Ingrese la cantidad de columnas deseadas: ')))
        break
    except ValueError:
        input('No se puede obtener el valor deseado, intentelo de nuevo...')
bandera = True
clear()
# ((j % 2 == 0) & (i % 2 != 0)) or ((j % 2 != 0) & (i % 2 == 0))
for i in range(m):
    for j in range(n):
        if bandera:
            print('\x1b[0;32;47m' + '   ' + '\x1b[0m', end="")
            bandera = not bandera
        else:
            print('\x1b[0;32;42m' + '   ' + '\x1b[0m', end="")
            bandera = not bandera
    print()
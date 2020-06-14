import os
clear = lambda: os.system('cls')

tamanios = {
    '1': 'Pez en buenas condiciones.',
    '2': 'Pez con problemas de nutrición.',
    '3': 'Pez con síntomas de organismo contaminado.',
    '4': 'Pez contaminado.'
}

while True:
    try:
        clear()
        print('Seleccione el tamaño del pez')
        print('1 - Normal.')
        print('2 - Por debajo de lo normal.')
        print('3 - Un poco por encima de lo normal.')
        print('4 - Sobredimensionado.')
        tamanioDelPez = input('Opcion: ')
        print(tamanios[tamanioDelPez])
        break
    except KeyError:
        input('La opcion no existe, intente de nuevo...')


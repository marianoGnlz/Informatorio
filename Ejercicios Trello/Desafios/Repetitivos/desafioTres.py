import os
clear = lambda: os.system('cls')

tiposDeDescuentos = {
    '1': 0.6,
    '2': 0.75,
    '3': 1.0
}

opciones = {
    '1': 'Calcular nuevo monto',
    '2': 'Salir'
}


while True:
    monto = 0
    descuento = 0
    while True:
        try:
            clear()
            print('Elija una opción')
            print('1 - Calcular nuevo monto.')
            print('2 - Salir.')
            opcion = opciones[input('Opción: ')]
            break
        except KeyError:
            input('Opcion no encontrada, intentelo de nuevo')
    if (opcion == 'Calcular nuevo monto'):
        while True:
            try:
                clear()
                monto = int(input('Ingrese el monto del cliente: '))
                break
            except ValueError:
                input('El monto ingresado es incorrecto, intentelo de nuevo...')
        while True:
            try:
                clear()
                print('Elija el código de descuento')
                print('1 - Rojo')
                print('2 - Amarillo')
                print('3 - Blanco')
                descuento = tiposDeDescuentos[input('Opción: ')]
                break
            except KeyError:
                input('Opcion no encontrada, intentelo de nuevo...')
        print('El monto a pagar es: ', monto*descuento)
        input('Presione enter para continuar...')
    elif opcion == 'Salir':
        break



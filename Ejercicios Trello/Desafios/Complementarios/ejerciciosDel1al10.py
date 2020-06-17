import os
clear = lambda: os.system('cls')


def handleInteger(frase):
    while True:
        try:
            clear()
            return int(input(frase))
        except ValueError:
            input('No se puede obtener el valor ingresado, intentelo de nuevo...')


def ejercicioUno():
    arrayNumeros = []

    arrayNumeros.append(handleInteger('Ingrese un número: '))
    arrayNumeros.append(handleInteger('Ingrese un número: '))
    arrayNumeros.append(handleInteger('Ingrese un número: '))

    clear()

    arrayNumeros.sort()
    arrayNumeros.reverse()
    for numero in arrayNumeros:
        print(f'{numero}')

def ejercicioDos():
    if (handleInteger('Ingrese un número: ') % 2 == 0):
        print('Es par.')
    else:
        print('No es es par.')

def ejercicioTres():
    numeroUno = handleInteger('Ingrese el primer número: ')
    numeroDos = handleInteger('Ingrese el segundo número: ')
    numeroTres = handleInteger('Ingrese el tercer número: ')

    if(numeroUno < numeroDos and numeroUno < numeroTres):
        print('El primer número es menor que los otros dos.')
    else:
        print('El primer número no es menor que alguno de los otros dos.')

def ejercicioCuatro():
    numeroN = handleInteger('Ingrese un número N: ')
    numeroM = handleInteger('Ingrese un número M: ')
    if (numeroM % numeroN == 0):
        print(f'{numeroN} es divisor de {numeroM}')
    else:
        print(f'{numeroN} no es divisor de {numeroM}')

def ejercicioCinco():
    lados = []
    lados.append(handleInteger('Ingrese el primer lado de un triángulo: '))
    lados.append(handleInteger('Ingrese el segundo lado de un triángulo: '))
    lados.append(handleInteger('Ingrese el tercer lado de un triángulo: '))

    lados.sort()
    lados.reverse()

    if (lados[0] >= lados[1] + lados[2]):
        print('No es un triángulo, porque A >= B + C.')
    elif (lados[0]**2 == lados[1]**2 + lados[2]**2):
        print('Se trata de un triángulo rectángulo, porque A^2 = B^2 + C^2.')
    elif (lados[0]**2 > lados[1]**2 + lados[2]**2):
        print('Se trata de un triángulo obtusángulo, porque A^2 > B^2 + C^2.')
    else:
        print('Se trata de un triángulo acutángulo, porque A^2 < B^2 + C^2.')

def ejercicioSeis():
    aumentos = {
        1: 1.15,
        2: 1.10,
        3: 1.06,
        4: 1
    }
    sueldoActual = abs(handleInteger('Ingrese el sueldo actual del jugador: '))

    if (sueldoActual <= 6000):
        print(f'El jugador obtendr un aumento del 15%, su sueldo actual es {sueldoActual} y su sueldo aumentado será {round(sueldoActual*aumentos[1])}.')
    elif (sueldoActual <= 7900):
        print(f'El jugador obtendr un aumento del 15%, su sueldo actual es {sueldoActual} y su sueldo aumentado será {round(sueldoActual*aumentos[2])}.')
    elif (sueldoActual <= 12000):
        print(f'El jugador obtendr un aumento del 15%, su sueldo actual es {sueldoActual} y su sueldo aumentado será {round(sueldoActual*aumentos[3])}.')
    else:
        print(f'El jugador obtendr un aumento del 15%, su sueldo actual es {sueldoActual} y su sueldo aumentado será {round(sueldoActual*aumentos[4])}.')
    
def ejercicioSiete():
    montoDeLaCompra = handleInteger('Ingrese el monto de la compra: ')
    if (montoDeLaCompra > 1000):
        print(f'Por haber superado los $1000 en su compra se le aplicará un descuento del 15%, quedándole un total de ${round(montoDeLaCompra*0.85)} finales.')
    else:
        print(f'No ha superado los $1000 en su compra, deberá abonar {montoDeLaCompra}')

def ejercicioOcho():
    edad = abs(handleInteger('Ingrese la edad de la persona: '))
    print(f'El número de pulsaciones será: {(220-edad) / 10}')

def ejercicioNueve():
    presupuestos = {
        1: 0.6,
        2: 0.2,
        3: 0.2
    }

    montoPresupuestal = abs(handleInteger('Ingrese el monto presupuestal: '))

    print(f'El monto presupuestal para el área de Pediatría será de: {round(montoPresupuestal*presupuestos[1])}')
    print(f'El monto presupuestal para el área de Traumatología será de: {round(montoPresupuestal*presupuestos[2])}')
    print(f'El monto presupuestal para el área de Kinesiología será de: {round(montoPresupuestal*presupuestos[3])}')

def ejercicioDiez():
    inversionUno = abs(handleInteger('Ingrese el monto del inversionista uno: '))
    inversionDos = abs(handleInteger('Ingrese el monto del inversionista dos: '))
    inversionTres = abs(handleInteger('Ingrese el monto del inversionista tres: '))

    inversionTotal = inversionDos + inversionUno + inversionTres

    print(f'La primer persona invirtió {round(inversionUno*100/inversionTotal)}%, respecto del total.')
    print(f'La segunda persona invirtió {round(inversionDos*100/inversionTotal)}%, respecto del total.')
    print(f'La tercera persona invirtió {round(inversionTres*100/inversionTotal)}%, respecto del total.')


ejercicios = {
    '1': lambda: ejercicioUno(),
    '2': lambda: ejercicioDos(),
    '3': lambda: ejercicioTres(),
    '4': lambda: ejercicioCuatro(),
    '5': lambda: ejercicioCinco(),
    '6': lambda: ejercicioSeis(),
    '7': lambda: ejercicioSiete(),
    '8': lambda: ejercicioOcho(),
    '9': lambda: ejercicioNueve(),
    '10': lambda: ejercicioDiez()
}


def main():
    while True:
        try:
            clear()
            print('Seleccione un ejercicio')
            print('1 - Numero de mayor a menor.')
            print('2 - Par o impar.')
            print('3 - Comparar tres números.')
            print('4 - N es divisor de M?')
            print('5 - Determinar que tipo de triángulo es.')
            print('6 - Determinar el aumento de un jugador, dado su sueldo.')
            print('7 - Determinar el monto final de una compra.')
            print('8 - Número de pulsaciones de una persona.')
            print('9 - Presupuesto del Centro Asistencial.')
            print('10 - Porcentaje de inversión de tres personas.')
            opcion = input('Opción: ')

            ejercicios[opcion]()
            break
        except KeyError:
            input('Opción no encontrada, intentelo de nuevo...')






main()
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
    clear()
    numeroMayor = -9999999999
    for i in range(9):
        numero = handleInteger('Ingrese un número: ')
        if (numero > numeroMayor):
            numeroMayor = numero
    print(f'El número mas grande es: {numeroMayor}')

def ejercicioDos():
    # Desarrollo en serie: (n/6)*(n+1)*(2n+1)
    n = handleInteger('Ingrese el n: ')
    resultado = 0
    for i in range(1,n+1):
        resultado += i**2
    
    print(f'El resultado es: {resultado}')

def ejercicioTres():
    AEsNegativo, BEsNegativo = False, False
    A = handleInteger('Ingrese un número A: ')
    if (A < 0):
        A = A * -1
        AEsNegativo = True
    B = handleInteger('Ingrese un número B: ')
    if (B < 0):
        B = B * -1
        BEsNegativo = True
    
    if (A == 0 or B == 0):
        print('El resultado es: 0.')
    else:
        resultado = 0
        while (B > 0):
            resultado += A
            B -= 1
        if(AEsNegativo and not BEsNegativo) or (not AEsNegativo and BEsNegativo):
            print(f'El resultado es: {resultado*-1}')
        else:
            print(f'El resultado es: {resultado}')

def ejercicioCuatro():
    for i in range(100,-1,-1):
        print(i)

def ejercicioCinco():
    bandera = '1'
    while bandera != '0':
        clear()
        numero = int(input('Ingrese un número: '))
        if (numero % 2 == 0):
            print('El número es par.')
        else:
            print('El número no es par.')
        print('Desea continuar?')
        print('0 - No.')
        print('1 - Si.')
        opcion = input('Opción: ')
        if (opcion == '0'):
            bandera = '0'

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
            print('1 - Número mayor de 10 números.')
            print('2 - Sumatoria del cuadrado de los primeros n naturales.')
            print('3 - Producto entre A y B.')
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
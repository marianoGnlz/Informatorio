import os
clear = lambda: os.system('cls')


def handleInteger():
    while True:
        try:
            clear()
            return int(input('Ingrese un número: '))
        except ValueError:
            input('No se puede obtener el valor ingresado, intentelo de nuevo...')


def ejercicioUno():
    arrayNumeros = []

    arrayNumeros.append(handleInteger())
    arrayNumeros.append(handleInteger())
    arrayNumeros.append(handleInteger())

    clear()

    arrayNumeros.sort()
    arrayNumeros.reverse()
    for numero in arrayNumeros:
        print(f'{numero}')

def ejercicioDos():
    if (handleInteger() % 2 == 0):
        print('Es par.')
    else:
        print('No es es par.')

def ejercicioTres():
    numeroUno = handleInteger()
    numeroDos = handleInteger()
    numeroTres = handleInteger()

    if(numeroUno < numeroDos and numeroUno < numeroTres):
        print('El primer número es menor que los otros dos.')
    else:
        print('El primer número no es menor que alguno de los otros dos.')

def ejercicioCuatro():
    numeroN = handleInteger()
    numeroM = handleInteger()
    if (numeroM % numeroN == 0):
        print(f'{numeroN} es divisor de {numeroM}')
    else:
        print(f'{numeroN} no es divisor de {numeroM}')

def ejercicioCinco():
    lados = []
    lados.append(handleInteger())
    lados.append(handleInteger())
    lados.append(handleInteger())

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

ejercicios = {
    '1': lambda: ejercicioUno(),
    '2': lambda: ejercicioDos(),
    '3': lambda: ejercicioTres(),
    '4': lambda: ejercicioCuatro(),
    '5': lambda: ejercicioCinco()
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
            opcion = input('Opción: ')

            ejercicios[opcion]()
            break
        except KeyError:
            input('Opción no encontrada, intentelo de nuevo...')






main()
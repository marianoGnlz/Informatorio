import os
clear = lambda: os.system('cls')

''' 
    -----------------------------------------------------------------
    Ejercicio para practicar asignación de datos e 
    impresión de cálculos por pantalla por lo que no
    deben utilizar estructuras de control solo deben solicitar datos
    hacer el calculo e imprimirlo.
    -----------------------------------------------------------------
    EJERCICIO 1: 
    Un automóvil puede cubrir una distancia de N kilómetros por día. 
    ¿Cuántos días tomará cubrir una ruta de longitud M kilómetros? 
    El programa obtiene dos números: N y M.
    Muestra por pantalla la respuesta a la pregunta
'''
# Coloque la resolución del Ejercicio 1 debajo de esta línea

def ejercicioUno():
    kilometrosPorDia = float(input('Ingrese la cantidad de kilometros por día que recorre: '))
    kilometrosTotales = float(input('Ingrese la cantidad de kilometros que desea recorrer: '))
    print(f'Tardará en recorrer {kilometrosTotales}km, {kilometrosTotales/kilometrosPorDia} días.')

'''
    -----------------------------------------------------------------
    Ejercicio simple para practicar Estructuras de control.
    Para resolver este ejercicio deberá utilizar estructuras 
    condicionales.
    -----------------------------------------------------------------
    EJERCICIO 2: 
    Escribir un algoritmo que lea tres numeros y me diga, si se trata 
    de un triangulo (La suma de dos lados cualesquiera debe ser mayor que el tercer lado), 
    y que tipo de triangulo es (Equilatero: todos los lados son iguales, 
    Isosceles: al menos dos lados son iguales, Escaleno: no tiene dos lados iguales).
'''
# Coloque la resolución del Ejercicio 2 debajo de esta línea
def ejercicioDos():
    clear()
    ladoUno = float(input('Ingrese el primer lado del triángulo: '))
    ladoDos = float(input('Ingrese el segundo lado del triángulo: '))
    ladoTres = float(input('Ingrese el tercer lado del triángulo: '))
    if(ladoUno + ladoDos > ladoTres):
        if(ladoUno == ladoDos == ladoTres):
            print('Es un triángulo equitalero.')
        elif (ladoUno == ladoDos != ladoTres) or (ladoUno == ladoTres != ladoDos) or (ladoTres == ladoDos != ladoUno):
            print('Es un triángulo isósceles.')
        else:
            print('Es un triángulo escaleno.')
    else:
        print('No es un triángulo.')
'''
    -----------------------------------------------------------------
    Ejercicio simple para practicar Estructuras de control.
    Para resolver este ejercicio deberá utilizar estructuras 
    repetitivas.
    -----------------------------------------------------------------
    EJERCICIO 3: 
    Solicitar el ingreso de números al usuario y emitir un 
    mensaje para determinar si es par o impar. 
    El ciclo debe finalizar cuando el usuario ingresa 0.
'''
# Coloque la resolución del Ejercicio 3 debajo de esta línea
def ejercicioTres():
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
'''
    -----------------------------------------------------------------
    Ejercicio Desafío.
    Deberá aplicar las estructuras de control que crea conveniente
    para resolver el ejercicio, puede ser condicional/repetitiva
    o una mezcla de ambas.
    -----------------------------------------------------------------
    EJERCICIO 4: 
    Crear un programa que permita al usuario ingresar los montos 
    de las compras de un cliente (se desconoce la cantidad de datos 
    que cargará, la cual puede cambiar en cada ejecución), cortando 
    el ingreso de datos cuando el usuario ingrese el monto 0.
    Si ingresa un monto negativo, no se debe procesar y se debe 
    pedir que ingrese un nuevo monto. Al finalizar, informar el total 
    a pagar teniendo que cuenta que, si las ventas superan el total 
    de $1000, se le debe aplicar un 10% de descuento.
'''
# Coloque la resolución del Ejercicio 4 debajo de esta línea
def ejercicioCuatro():
    bandera = True
    montoTotal = 0
    while bandera:
        clear()
        monto = float(input('Ingrese el monto de la compra: '))
        if (monto < 0):
            print('El monto ingresado es negativo, ingréselo de nuevo...')
        else:
            montoTotal = montoTotal + monto
            print('Desea continuar?')
            print('0 - No.')
            print('1 - Si.')
            opcion = input('Opcion: ')
            if (opcion == '0'):
                bandera = False
    
    if(montoTotal > 1000):
        print(f'El monto total es ${montoTotal*0.9}')
    else:
        print(f'El monto total es ${montoTotal}')





ejercicios = {
    '1': lambda: ejercicioUno(),
    '2': lambda: ejercicioDos(),
    '3': lambda: ejercicioTres(),
    '4': lambda: ejercicioCuatro()
}
def main():
    while True:
        try:
            clear()
            print('Seleccione un ejercicio:')
            print('1 - Ejercicio uno.')
            print('2 - Ejercicio dos.')
            print('3 - Ejercicio tres.')
            print('4 - Ejercicio cuatro.')
            opcion = input('Opción: ')
            ejercicios[opcion]()
            break
        except KeyError:
            input('Opción no encotrada, intentelo de nuevo....')

main()
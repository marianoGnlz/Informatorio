import os
clear = lambda: os.system('cls')


def handleInteger(frase):
    while True:
        try:
            clear()
            return int(input(frase))
        except ValueError:
            input('No se puede obtener el valor ingresado, intentelo de nuevo...')
        
def handleFloat(frase):
    while True:
        try:
            clear()
            return float(input(frase))
        except ValueError:
            input('No se puede obtener el valor ingresado, intentelo de nuevo...')


def ejercicioOnce():
    notaUno = abs(handleFloat('Ingrese la primer nota del alumno: '))
    notaDos = abs(handleFloat('Ingrese la segunda nota del alumno: '))
    notaTres = abs(handleFloat('Ingrese la tercer nota del alumno: '))

    promedio = (notaUno + notaDos + notaTres) / 3

    if promedio >= 70:
        print(f'El alumno ha aprobado, su nota es: {round(promedio)}')
    else:
        print(f'El alumno ha desaprobado, su nota es: {round(promedio)}')

def ejercicioDoce():
    claves = {
        '1': 0.9,
        '2': 0.8
    }

    nombre = input('Ingrese el nombre del artículo: ')
    precio = abs(handleFloat('Ingrese el precio del artículo: '))
    
    while True:
        try:
            print('Seleccione una opción')
            print('1 - Clave: 01')
            print('2 . Clave: 02')
            opcion = input('Opción: ')
            claves[opcion]
            break
        except KeyError:
            input('Opción no encontrada, por favor intentelo de nuevo...')

    print(f'El artículo {nombre}, de clave 0{opcion}, tiene un precio de {precio} pesos y su precio con descuento es {round(precio*claves[opcion])}')

def ejercicioTrece():
    precio = abs(handleInteger('Ingrese el precio del producto: '))
    numeroAlAzar = handleInteger('Ingrese un número al azar: ')
    if (numeroAlAzar < 74):
        print(f'Ha obtenido un descuento del 15%, el precio final es {round(precio*0.85)}')
    else:
        print(f'Ha obtenido un descuento del 20%, el precio final es {round(precio*0.8)}')

def ejercicioCatorce():
    numeroUno = handleInteger('Ingrese el primer número: ')
    numeroDos = handleInteger('Ingrese el segundo número: ')
    if (numeroUno == numeroDos):
        print(f'Los números son iguales, su multiplicación es: {numeroUno*numeroDos}')
    elif (numeroUno < numeroDos):
        print(f'El primero es más chico que el segundo, su resta es: {numeroUno-numeroDos}')
    else:
        print(f'El primero es más grande que el segundo, su sumas es: {numeroUno+numeroDos}')

def ejercicioQuince():
    horasTrabajadas = abs(handleInteger('Ingrese la cantidad de horas trabajadas: '))

    if (horasTrabajadas <= 40):
        print(f'Trabajó {horasTrabajadas} horas, su sueldo es de ${horasTrabajadas*16}')
    else:
        print(f'Trabajó {horasTrabajadas} horas, su sueldo es de ${40*16 + ((horasTrabajadas-40)*20)}')

def ejercicioDieciseis():
    numeroDeCamisas = abs(handleInteger('Ingrese el número de camisas compradas: '))
    precioTotal = abs(handleFloat('Ingrese el monto total: '))

    if(numeroDeCamisas >= 3):
        print(f'El monto final es %{round(precioTotal*0.8)}')
    else:
        print(f'El monto fianl es %{round(precioTotal*0.9)}')

def ejercicioDiecisiete():
    sexos = {
        '1': 1.65,
        '2': 1.72
    }
    while True:
        try:
            print('Seleccione su sexo: ')
            print('1 - Mujer')
            print('2 - Hombre')
            sexo = input('Opción:')
            break
        except KeyError:
            input('Opción no encontrada, intentelo de nuevo...')
    
    altura = abs(handleFloat('Ingrese su altura: '))

    if (sexo == '1'):
        if (altura > sexos[sexo]):
            print('Su altura está por encima de la media de las mujeres.')
        else:
            print('Su altura no supera la media de las mujeres.')
    else:
        if (altura > sexos[sexo]):
            print('Su altura está por encima de la media de los hombres.')
        else:
            print('Su altura no supera la media de los hombres.')

def ejercicioDieciocho():
    ladoUno = abs(handleFloat('Ingrese el tamaño del primer lado: '))
    ladoDos = abs(handleFloat('Ingrese el tamaño del segundo lado: '))
    ladosTres = abs(handleFloat('Ingrese el tamaño del tercer lado: '))

    if (ladoUno == ladoDos and ladoUno == ladosTres):
        print('Se trata de un triángulo equilátero.')
    elif (ladoUno == ladoDos or ladoUno == ladosTres or ladosTres == ladoDos):
        print('Se trata de un triángulo isósceles.')
    else:
        print('Se trata de un triángulo escaleno.')

def ejercicioDiecinueve():
    tipoCliente = {
        '1':'p',
        '2':'l'
    }

    importeBruto = abs(handleFloat('Ingrese el importe bruto de la compra: '))
    while True:
        try:
            clear()
            print('Seleccione un tipo de cliente')
            print('1 - Librería.')
            print('2 - Particular.')
            opcion = input('Opción: ')
            tipoCliente[opcion]
            break
        except KeyError:
            input('Opción no encontrada, intentelo de nuevo....')
    cantidadDeLibrosPedidos = abs(handleInteger('Ingrese la cantidad de libros pedidos: '))

    if (opcion == '1'):
        if (cantidadDeLibrosPedidos > 24):
            print(f'El importe final es: ${round(importeBruto*0.75)}')
        else:
            print(f'El importe final es: ${round(importeBruto*0.8)}')
    else:
        if (cantidadDeLibrosPedidos > 18):
            print(f'El importe final es: ${round(importeBruto*0.9)}')
        elif (cantidadDeLibrosPedidos > 6):
            print(f'El importe final es: ${round(importeBruto*0.95)}')
        else:
            print(f'El importe final es: ${importeBruto}')
        

ejercicios = {
    '11': lambda: ejercicioOnce(),
    '12': lambda: ejercicioDoce(),
    '13': lambda: ejercicioTrece(),
    '14': lambda: ejercicioCatorce(),
    '15': lambda: ejercicioQuince(),
    '16': lambda: ejercicioDieciseis(),
    '17': lambda: ejercicioDiecisiete(),
    '18': lambda: ejercicioDieciocho(),
    '19': lambda: ejercicioDiecinueve()
}

def main():
    while True:
        try:
            clear()
            print('Seleccione un ejercicio')
            print('11 - Determinar si un alumno reprueba o no, dato tres notas.')
            print('12 - Descuento de un artículo.')
            print('13 - Promoción de un supermercado.')
            print('14 - Dados dos números: multiplicarlos, restarlos o sumarlos.')
            print('15 - Salario semanal de un obrero.')
            print('16 - Descuento de las camisas.')
            print('17 - Determinar la altura de una persona.')
            print('18 - Tipo de triángulo.')
            print('19 - Distribuidora de libros.')
            opcion = input('Opción: ')

            ejercicios[opcion]()
            break
        except KeyError:
            input('Opción no encontrada, intentelo de nuevo...')






main()
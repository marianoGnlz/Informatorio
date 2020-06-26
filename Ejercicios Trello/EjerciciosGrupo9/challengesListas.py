def ejercicioUno():
    palabra = input('Ingrese una palabra: ').lower()
    cantidadDeA = palabra.count('a')
    cantidadDeE = palabra.count('e')
    cantidadDeI = palabra.count('i')
    cantidadDeO = palabra.count('o')
    cantidadDeU = palabra.count('u')
    print(f'La cantidad de a son {cantidadDeA}')
    print(f'La cantidad de e son {cantidadDeE}')
    print(f'La cantidad de i son {cantidadDeI}')
    print(f'La cantidad de o son {cantidadDeO}')
    print(f'La cantidad de u son {cantidadDeU}')

def ejercicioDos():
    listaDePalabras = []
    while True:
        palabraIngresada = input('Ingrese una palabra: ')
        listaDePalabras.append(palabraIngresada)
        print('Desea continuar? \n1 - Si.\n2 - No.')
        opcion = input('Opción: ')
        if (opcion == '2'):
            break
    while True:
        try:
            palabraUno = input('Ingrese una palabra que esté en la lista: ')
            indexDePalabraUno = listaDePalabras.index(palabraUno)
            break
        except ValueError:
            input(f'"{palabraUno}" no se encuentra en la lista, intentelo de nuevo....')
    palabraDos = input('Ingrese una palabra de reemplazo: ')
    listaDePalabras[indexDePalabraUno] = palabraDos
    print(listaDePalabras)

        

ejercicios = {
    '1':lambda: ejercicioUno(),
    '2':lambda: ejercicioDos()
}

opcion = input('Ejercicio: ')
ejercicios[opcion]()
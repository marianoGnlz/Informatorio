def ejercicioUno():
    tupla = (1,2,3,4,5,6,7,8,9,10)
    indice = int(input('Ingrese un índice, para conocer su valor: '))
    print(tupla[indice])

def ejercicioDos():
    diccionario = {}
    print('Ingrese las palabras, en formato <palabra>:<traducción>, separados por , (coma)')
    paresDePalabras = 'manzana:apple,pera:pear,durazno:peach,banana:banana'
    # paresDePalabras = input(f'Pares: ')
    listaDePalabras = paresDePalabras.split(',')
    # ['manzana:apple'|pera:pear|durazno:peach|banana:banana]
    for par in listaDePalabras:
        parSeparado = par.split(':')
        diccionario.update({parSeparado[0]:parSeparado[1]})
    frase = input('Ingrese una frase para traducirla: ')
    for key,palabras in diccionario.items():
        fraseTraducida = frase.replace(key,palabras)
        frase = fraseTraducida
    print(fraseTraducida)


ejercicios = {
    '1': lambda: ejercicioUno(),
    '2': lambda: ejercicioDos()
}
ejecutar = input('1 - Ejercicio uno. \n2 - Ejercicio dos. \n3 - Ejercicio tres. \nOpción: ')
ejercicios[ejecutar]()

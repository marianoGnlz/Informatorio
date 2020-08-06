import random
listaDePalabras = ['manzana', 'pera','banana','durazno']

def palabraAGuionBajo(palabra):
    return "_"*len(palabra)

def controlLetra(palabra,letra,palabraConGuiones):
    if letra in palabra:
        while letra in palabra:
            posicion = palabra.index(letra)
            palabraConGuiones[posicion] = letra
            palabra = palabra.replace(letra,'#',1)
        return 0
    else:
        return -1

def controlDeGuiones(palabraConGuiones):
    return "_" not in palabraConGuiones


def main():
    numeroDeIntentos = 6
    palabra = random.choice(listaDePalabras)
    palabraConGuiones = list(palabraAGuionBajo(palabra))
    print(f'\x1b[0;32;12mPalabra: {palabraConGuiones}\x1b[0m')
    while numeroDeIntentos > 0:
        letra = input('Ingrese una letra: ').lower()
        numeroDeIntentos += controlLetra(palabra,letra,palabraConGuiones)
        print(f'\x1b[0;32;12m{palabraConGuiones}\x1b[0m')
        if(controlDeGuiones(palabraConGuiones)):
            return print('Ganaste.')
        opcion = input('Desea arriesgar? Si/No ').lower()
        if(opcion == 'si'):
            palabraArriesgada = input('Ingrese una palabra: ').lower()
            if(palabra == palabraArriesgada):
                return print('Ganaste.')
            else:
                numeroDeIntentos = 0
        print(f'Intentos restantes {numeroDeIntentos}')
    else:
        print('Perdiste.')
        
main()


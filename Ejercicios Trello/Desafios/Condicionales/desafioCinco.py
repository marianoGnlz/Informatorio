import os
clear = lambda: os.system('cls')

tiposDeBarrios = {
    '1': 'Centrico',
    '2': 'No centrico'
}

while True:
    try:
        clear()
        nombreDelBarrio = input('Ingrese el nombre del barrio: ').lower()
        primeraLetra = nombreDelBarrio[0]
        print('Seleccione un tipo de barrio')
        print('1 - Centrico')
        print('2 - No centrico')
        tipoDelBarrio = tiposDeBarrios[input('Opción: ')]
        if (tipoDelBarrio == 'Centrico'):
            if (primeraLetra <= 'm'):
                print('El barrio se encuentra en la sección A.')
            else:
                print('El barrio se encuentra en la sección B.')
        else:
            if(primeraLetra >= 'm'):
                print('El barrio se encuentra en la sección A.')
            else:
                print('El barrio se encuentra en la sección B.')
        break
    except KeyError:
        input('Opción no encontrada, intentelo de nuevo...')
    except IndexError:
        input('No se puede obtener la inicial del nombre, intentelo de nuevo...')
import os
clear = lambda: os.system('cls')

ingredientesComunes = ['Verduras', 'Berenjena']

bandera = True

recetaUno = {
    '1': 'Lentejas',
    '2': 'Apio'
}
recetaDos = {
    '1': 'Morrón',
    '2': 'Cebolla'
}

recetas = {
    '1': recetaUno,
    '2': recetaDos
}

while bandera:
    try:
        clear()
        print('Elija el tipo de receta que desea')
        print('1 - Receta 1')
        print('2 - Receta 2')
        recetaElegida = recetas[input('Opcion: ')]

        print('Los ingredientes disponibles son:')
        for ingredientes in recetaElegida:
            print(f'{ingredientes} - {recetaElegida[ingredientes]}')

        ingredienteElegido = input('Seleccione una opción: ')
        ingredientesComunes.append(recetaElegida[ingredienteElegido])

        print('Los ingredientes finales son:')
        for ingredientes in ingredientesComunes:
            print(f'- {ingredientes}')
        
        bandera = False
    except KeyError:
        input('Error, opcion no encontrada, intentelo de nuevo...')

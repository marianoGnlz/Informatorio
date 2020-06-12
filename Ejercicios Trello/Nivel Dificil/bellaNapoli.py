import os
clear = lambda: os.system('cls')

ingredientesVegetarianos = {
    1: 'Pimiento',
    2: 'Rúcula'
}
ingredientesNoVegetarianos = {
    1: 'Jamón',
    2: 'Panceta'
}
pizzaBase = ['Tomate', 'Mozzarella']

while True:
    try:
        print('¿Qué tipo de pizza desea?')
        print('1 - Vegetariana.')
        print('2 - No Vegetariana.')
        print('Opcion: ', end='')
        opcion = int(input())
        if opcion == 1 or opcion == 2:
            break
        clear()
    except ValueError:
        print('No es un número válido. Intentelo de nuevo....')

if opcion == 1:
    while True:
        try:
            clear()
            print('==== Menu ====')
            for ingrediente in ingredientesVegetarianos:
                print(f'{ingrediente} - {ingredientesVegetarianos[ingrediente]}')
            print('Opcion: ', end='')
            opcion = int(input())
            if opcion == 1 or opcion == 2:
                break
        except ValueError:
            print('No es un número válido. Intentelo de nuevo....')
    pizzaBase.append(ingredientesVegetarianos[opcion])
else:
    while True:
        try:
            clear()
            print('==== Menu ====')
            for ingrediente in ingredientesNoVegetarianos:
                print(f'{ingrediente} - {ingredientesNoVegetarianos[ingrediente]}')
            print('Opcion: ', end='')
            opcion = int(input())
            if opcion == 1 or opcion == 2:
                break
        except ValueError:
            print('No es un número válido. Intentelo de nuevo....')
    pizzaBase.append(ingredientesNoVegetarianos[opcion])

print('Ingredientes: ')
for ingrediente in pizzaBase:
    print(f'- {ingrediente}')

    
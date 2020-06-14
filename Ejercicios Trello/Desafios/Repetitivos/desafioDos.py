personas = {
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0
}

totalDePersonas = 0

print('Desea añadir una persona')
print('1 - Si.')
print('2 - No.')
respuesta = input('Opción: ')
while respuesta == '1':
    totalDePersonas += 1
    print('Seleccione una opcion:')
    print('1 - Menos de 100 colillas')
    print('2 - Más de 100 colillas')
    print('3 - Menos de 200 colillas')
    print('4 - Más de 200 colillas')
    numeroDeColillas = input('Opción: ')
    personas.update({numeroDeColillas:personas.get(numeroDeColillas)+1})
    print('Desea continuar?')
    print('1 - Si.')
    print('2 - No.')
    respuesta = input('Opción: ')


print('El porcentaje de personas con menos de 100 colillas es: ', personas['1']*100 / totalDePersonas)
print('El porcentaje de personas con más de 100 colillas es: ', personas['2']*100 / totalDePersonas)
print('El porcentaje de personas con menos de 200 colillas es: ', personas['3']*100 / totalDePersonas)
print('El porcentaje de personas con más de 200 colillas es: ', personas['4']*100 / totalDePersonas)
    
    

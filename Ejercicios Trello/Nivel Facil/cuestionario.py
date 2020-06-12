print('Ingrese el número total de preguntas: ', end='')
cantidadDePreguntas = int(input())
print('Ingrese el número de preguntas correctas: ', end='')
cantidadDePreguntasCorrectas = int(input())

porcentajeDeAprobadas = (cantidadDePreguntasCorrectas * 100) / cantidadDePreguntas

if porcentajeDeAprobadas >= 90:
    print('Excelente.')
elif porcentajeDeAprobadas >= 70:
    print('Bueno.')
elif porcentajeDeAprobadas >= 60:
    print('Aprobado.')
else:
    print('No alcanzó.')

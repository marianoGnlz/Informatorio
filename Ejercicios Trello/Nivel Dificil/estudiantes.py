
print('Ingrese su nombre: ', end='')
nombreDelAlumno = input().lower()
print('Ingrese su turno: ', end='')
turnoDelAlumno = input().lower()
if turnoDelAlumno == 'tarde':
    if nombreDelAlumno[0] <= 'm':
        print('Pertenece al grupo A.')
    else:
        print('Pertenede al grupo B.')
elif turnoDelAlumno == 'noche':
    if nombreDelAlumno[0] >= 'n':
        print('Pertenece al grupo A.')
    else:
        print('Pertenede al grupo B.')
else:
    print('No pertenece a ningun grupo.')
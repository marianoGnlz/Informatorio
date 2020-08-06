class Abuelo():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

class Papa(Abuelo):
    def __init__(self,nombre,edad,dni):
        self._dni = dni
        Abuelo.__init__(self,nombre,edad)
    def obtenerDni(self):
        return self._dni

class Hijo(Papa):
    def __init__(self,nombre,edad,dni,apellido):
        Papa.__init__(self,nombre,edad,dni)
        self.apellido = apellido

hijo1 = Hijo('dani',2,344565,'sanchez')

print(hijo1._dni)
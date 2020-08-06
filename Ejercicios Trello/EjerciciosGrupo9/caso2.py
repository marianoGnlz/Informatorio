
class Vehiculo():
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas    

class Coche(Vehiculo):
    def __init__(self,velocidad,cilindrada):
        Vehiculo.__init__(self,color,ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return f'Mis atributos son: {self.velocidad} y {self.cilindrada}'

class Camioneta(Coche):
    def __init__(self,velocidad,cilindrada,carga):
        self.carga = carga
        Coche.__init__(velocidad,cilindrada)
    def __str__(self):
        return f'Mis atributos son: {self.carga}'

class Bicicleta(Vehiculo):
    def __init__(self,tipo):
        self.tipo = tipo
        # super().__init__(color,ruedas)
    def __str__(self):
        return f'Mis atributos son: {self.tipo}'

class Motocicleta(Bicicleta):
    def __init__(self,velocidad,cilindrada):
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        # super().__init__(tipo)
    def __str__(self):
        return f'Mis atributos son: {self.velocidad} y {self.cilindrada}'

camioneta1 = Camioneta()

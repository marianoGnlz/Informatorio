class Triangulo:
    def __init__(self,ladoA,ladoB,ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
    
    def ladoMayor(self):
        if (self.ladoA > self.ladoB and self.ladoA > self.ladoC):
            print(f'El lado mayor es: {self.ladoA}')
        elif (self.ladoB > self.ladoA and self.ladoB > self.ladoC):
            print(f'El lado mayor es: {self.ladoB}')
        else:
            print(f'El lado mayor es: {self.ladoC}')
    
    def determinarTriangulo(self):
        if (self.ladoA == self.ladoB and self.ladoA == self.ladoC):
            print(f'Triangulo equilatero.')
        elif (self.ladoA != self.ladoB and self.ladoA != self.ladoC and self.ladoB != self.ladoC):
            print(f'Triangulo escaleno.')
        else:
            print(f'Triangulo isosceles.')

ladoA = input('Ingrese un lado: ')
ladoB = input('Ingrese un lado: ')
ladoC = input('Ingrese un lado: ')

triangulo = Triangulo(ladoA,ladoB,ladoC)

triangulo.ladoMayor()
triangulo.determinarTriangulo()
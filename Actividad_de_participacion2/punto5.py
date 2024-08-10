class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Círculo:
    def __init__(self, centro, radio):
        self.centro = centro  
        self.radio = radio    

    def calcular_area(self):
        pi = 3.141592653589793
        return pi * (self.radio ** 2)

    def calcular_perimetro(self):
        pi = 3.141592653589793
        return 2 * pi * self.radio

    def punto_pertenece(self, punto):
     
        distancia_cuadrada = (punto.x - self.centro.x) ** 2 + (punto.y - self.centro.y) ** 2
        return distancia_cuadrada <= self.radio ** 2

centro = Punto(0, 0)
circulo = Círculo(centro, 5)



punto1 = Punto(3, 4)
punto2 = Punto(6, 8)


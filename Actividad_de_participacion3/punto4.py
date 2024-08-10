class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectángulo:
    def __init__(self, esquina1, esquina2):
        self.esquina1 = esquina1  
        self.esquina2 = esquina2  

    def calcular_perimetro(self):
        ancho = abs(self.esquina2.x - self.esquina1.x)
        alto = abs(self.esquina2.y - self.esquina1.y)
        return 2 * (ancho + alto)

    def calcular_area(self):
        ancho = abs(self.esquina2.x - self.esquina1.x)
        alto = abs(self.esquina2.y - self.esquina1.y)
        return ancho * alto

    def es_cuadrado(self):
        ancho = abs(self.esquina2.x - self.esquina1.x)
        alto = abs(self.esquina2.y - self.esquina1.y)
        return ancho == alto


p1 = Punto(0, 0)
p2 = Punto(4, 3)
rectangulo = Rectángulo(p1, p2)

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar(self):
        print(f"Coordenadas del punto: ({self.x}, {self.y})")

    def mover(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y

    def calcular_distancia(self, otro_punto):
        return ((self.x - otro_punto.x) ** 2 + (self.y - otro_punto.y) ** 2) ** 0.5


p1 = Punto(3, 4)
p2 = Punto(6, 8)

p1.mostrar()  
p2.mostrar() 

p1.mover(10, 10)  
p1.mostrar()  

distancia = p1.calcular_distancia(p2)  
print(f"Distancia entre los puntos: {distancia}")

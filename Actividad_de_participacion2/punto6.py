class Carta:
    CORAZONES = "Corazones"
    DIAMANTES = "Diamantes"
    TREBOLES = "Tréboles"
    PICAS = "Picas"

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

    def __str__(self):
        return f"{self.valor} de {self.pinta}"


carta1 = Carta(7, Carta.CORAZONES)
carta2 = Carta("Rey", Carta.PICAS)

print(carta1)  
print(carta2)  

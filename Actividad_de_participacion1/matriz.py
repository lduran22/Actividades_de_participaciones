import random

def generar_matriz(filas, columnas, valor_min=0, valor_max=10):

    matriz = []
    for _ in range(filas):
        fila = [random.randint(valor_min, valor_max) for _ in range(columnas)]
        matriz.append(fila)
    return matriz

def imprimir_matriz(matriz):

    for fila in matriz:
        print(" ".join(map(str, fila)))

filas = int(input("Introduce el número de filas: "))
columnas = int(input("Introduce el número de columnas: "))

matriz = generar_matriz(filas, columnas)

print("La matriz generada es:")
imprimir_matriz(matriz)

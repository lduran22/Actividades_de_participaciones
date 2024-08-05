def generar_pares(inicio, fin):

    pares = [numero for numero in range(inicio, fin + 1) if numero % 2 == 0]
    return pares


lista_pares = generar_pares(1, 100)
print("Lista de números pares entre 1 y 100:")
print(lista_pares)

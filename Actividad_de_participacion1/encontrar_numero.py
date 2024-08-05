def encontrar_mayor_y_menor(lista):
    mayor = max(lista)
    menor = min(lista)
    
    return (mayor, menor)

lista_numeros = [10, 5, 8, 23, -1, 42]  
mayor, menor = encontrar_mayor_y_menor(lista_numeros)
print(f"El número más grande en la lista es: {mayor}")
print(f"El número más pequeño en la lista es: {menor}")

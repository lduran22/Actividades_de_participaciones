def invertir_lista(lista):

    lista_invertida = lista[::-1]
    return lista_invertida

lista_original = [1, 2, 3, 4, 5] 
lista_invertida = invertir_lista(lista_original)
print(f"La lista original es: {lista_original}")
print(f"La lista invertida es: {lista_invertida}")

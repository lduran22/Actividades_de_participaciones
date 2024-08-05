def media_aritmetica(lista):

    if not lista:  # Verificar si la lista está vacía
        return 0

    suma = sum(lista)  # Sumar todos los elementos de la lista
    cantidad = len(lista)  # Contar el número de elementos en la lista
    return suma / cantidad  # Calcular y devolver la media

def es_palindromo(cadena):

    cadena_limpia = ''.join(c for c in cadena if c.isalnum()).lower()

    return cadena_limpia == cadena_limpia[::-1]


texto = input("Ingresa una cadena de texto: ")


if es_palindromo(texto):
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")

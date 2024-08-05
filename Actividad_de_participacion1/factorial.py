def factorial(n):
  
    if n < 0:
        print("El factorial no está definido para números negativos.")
    
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

numero = int(input("Introduce un número entero no negativo: "))

resultado = factorial(numero)
print(f"El factorial de {numero} es: {resultado}")

def fahrenheit_a_celsius(fahrenheit):

    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

temperatura_fahrenheit = float(input("Introduce la temperatura en grados Fahrenheit: "))
temperatura_celsius = fahrenheit_a_celsius(temperatura_fahrenheit)
print(f"{temperatura_fahrenheit} grados Fahrenheit son {temperatura_celsius:.2f} grados Celsius.")

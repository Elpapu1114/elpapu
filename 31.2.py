import random

elementos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

ganadores = random.sample(elementos, 4)

print("Números/letras ganadoras:")
print(ganadores)

print(f"\nSi tu boleto tiene {ganadores}, ¡ganaste un premio!")
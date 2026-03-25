import random

elementos = [1,2,3,4,5,6,7,8,9,10,'A','B','C','D','E']

my_ticket = [1, 'A', 5, 'C']

intentos = 0
ganado = False

while not ganado:
    intentos += 1
    ganador = random.sample(elementos, 4)
    
    if ganador == my_ticket:
        ganado = True

print(f"¡Ganaste después de {intentos} intentos!")
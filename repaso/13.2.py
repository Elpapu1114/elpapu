import random

colores = ["verde", "rojo", "amarillo"]

color_alien = random.choice(colores)

print("Color del alien:", color_alien)

if color_alien == "verde":
    print("Ganaste 5 puntos")
else:
    print("Ganaste 10 puntos")
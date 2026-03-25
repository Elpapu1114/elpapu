import random

colores = ["verde", "rojo", "amarillo","azul","marron","violeta" ]

color_alien = random.choice(colores)

print("Color del alien:", color_alien)

if color_alien == "verde":
    print("Ganaste 5 puntos")
elif color_alien == "amarillo":
    print("Ganaste 10 puntos")
elif color_alien == "rojo":
    print("Ganaste 15 puntos")
else:
    print("Ganaste 0 puntos")
import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        numero = random.randint(1, self.sides)
        print(numero)


print("Dado de 6 caras:")
d6 = Die()

for _ in range(10):
    d6.roll_die()


print("\nDado de 10 caras:")
d10 = Die(10)

for _ in range(10):
    d10.roll_die()


print("\nDado de 20 caras:")
d20 = Die(20)

for _ in range(10):
    d20.roll_die()
invitados = ["paredes", "aranda", "ascasibar", "delgado"]

import random
import time

def enviar_invitaciones():
    for persona in invitados:
        print(f"Hola {persona}, ¿querés venir a comer un asado a mi casa?")
        time.sleep(1)

    ausente = random.choice(invitados)
    print(f"{ausente} no va a poder venir")
    time.sleep(1)

    invitados.remove(ausente)
    print(invitados)


def agregar_invitados():
    time.sleep(2)
    print("Conseguimos un lugar más grande para comer")
    time.sleep(1)

    invitados.insert(0, "bareiro")
    invitados.insert(2, "ayrton")
    invitados.insert(-1, "gorosito")

    print(invitados)


def programa_principal():
    enviar_invitaciones()
    agregar_invitados()


programa_principal()
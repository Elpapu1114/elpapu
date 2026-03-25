mascota1 = {
    "animal": "perro",
    "dueño": "jeffrey"
}

mascota2 = {
    "animal": "elefante",
    "dueño": "rick"
}

mascota3 = {
    "animal": "pato",
    "dueño": "Papu"
}

mascotas = [mascota1, mascota2, mascota3]

for mascota in mascotas:
    print(f"Animal: {mascota['animal']}")
    print(f"Dueño: {mascota['dueño']}\n")
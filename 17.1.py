persona1 = {
    "Nombre": "Rick",
    "Edad": 67,
    "Ciudad": "Yankerlandia",
}
persona2 = {
    "nombre": "Papu",
    "edad": 30,
    "ciudad": "Lima"
}

persona3 = {
    "nombre": "Jeffrey",
    "edad": 20,
    "ciudad": "Houton"
}

gente = [persona1, persona2, persona3]

for persona in gente:
    print(f"Nombre: {persona['nombre']}")
    print(f"Edad: {persona['edad']}")
    print(f"Ciudad: {persona['ciudad']}\n")
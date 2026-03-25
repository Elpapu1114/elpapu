lenguajes_favoritos = {
    "Juan": "python",
    "Sara": "c",
    "Eduardo": "rust",
    "Agustina": "c#"
}

personas = ["Juan", "Pedro", "Sara", "Lucia", "Agustina", "Martin"]

for persona in personas:
    if persona in lenguajes_favoritos:
        print(f"Gracias por responder la encuesta, {persona}.")
    else:
        print(f"{persona}, te invitamos a participar en la encuesta.")
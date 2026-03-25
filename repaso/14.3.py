usuarios_actuales = ["admin", "jeffrey", "papu", "esteban", "robert"]


usuarios_nuevos = ["Rafael", "kevin", "diddy", "larry", "paulo"]

usuarios_actuales_lower = [usuario.lower() for usuario in usuarios_actuales]

for usuario in usuarios_nuevos:
    if usuario.lower() in usuarios_actuales_lower:
        print(f"El nombre de usuario '{usuario}' ya está en uso, elegí otro.")
    else:
        print(f"El nombre de usuario '{usuario}' está disponible.")
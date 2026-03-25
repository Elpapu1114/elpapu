usuarios = ["admin", "jeffrey", "papu", "esteban", "robert"]

if not usuarios:
    print("¡Necesitamos encontrar algunos usuarios!")
else:
    for usuario in usuarios:
        if usuario == "admin":
            print("Hola admin, ¿querés ver un informe de estado?")
        else:
            print(f"Hola {usuario}, gracias por volver a iniciar sesión.")
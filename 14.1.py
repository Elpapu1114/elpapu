usuarios = ["admin", "jeffrey", "papu", "esteban", "robert"]

for usuario in usuarios:
    if usuario == "admin":
        print("Hola admin, ¿querés ver un informe de estado?")
    else:
        print(f"Hola {usuario}, gracias por volver a iniciar sesión.")
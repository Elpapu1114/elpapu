import json

def obtener_usuario():
    try:
        with open("usuario.json") as archivo:
            nombre = json.load(archivo)
    except FileNotFoundError:
        return None
    else:
        return nombre

def obtener_nuevo_usuario():
    nombre = input("¿Cómo te llamás? ")
    with open("usuario.json", "w") as archivo:
        json.dump(nombre, archivo)
    return nombre

def saludar_usuario():
    nombre = obtener_usuario()

    if nombre:
        respuesta = input(f"¿Sos {nombre}? (s/n) ")
        if respuesta.lower() == "s":
            print(f"¡Bienvenido de nuevo, {nombre}!")
        else:
            nombre = obtener_nuevo_usuario()
            print(f"¡Te voy a recordar, {nombre}!")
    else:
        nombre = obtener_nuevo_usuario()
        print(f"¡Te voy a recordar, {nombre}!")

saludar_usuario()
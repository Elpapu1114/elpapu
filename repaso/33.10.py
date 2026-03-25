import json

archivo_nombre = "usuario.json"

nombre = input("¿Cómo te llamás? ")
edad = input("¿Cuántos años tenés? ")
ciudad = input("¿De qué ciudad sos? ")

usuario = {
    "nombre": nombre,
    "edad": edad,
    "ciudad": ciudad
}

with open(archivo_nombre, "w") as archivo:
    archivo.write(json.dumps(usuario))

with open(archivo_nombre, "r") as archivo:
    contenido = archivo.read()
    datos = json.loads(contenido)

print("\nResumen:")
print(f"Nombre: {datos['nombre']}")
print(f"Edad: {datos['edad']}")
print(f"Ciudad: {datos['ciudad']}")
import json

archivo_nombre = "numero_favorito.json"

try:
    with open(archivo_nombre, "r") as archivo:
        numero = json.load(archivo)

except (FileNotFoundError, json.JSONDecodeError):
    numero = input("¿Cuál es tu número favorito? ")
    
    with open(archivo_nombre, "w") as archivo:
        json.dump(numero, archivo)
    
    print("¡Voy a recordar tu número favorito!")

else:
    print(f"¡Sé cuál es tu número favorito! Es {numero}.")
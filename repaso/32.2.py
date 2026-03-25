from pathlib import Path

path = Path("learning_python.txt")

contenido = path.read_text()
print("Leyendo todo el archivo:")
print(contenido)

print("\nLeyendo línea por línea:")
lineas = contenido.splitlines()

for linea in lineas:
    print(linea)
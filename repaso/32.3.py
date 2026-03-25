from pathlib import Path

path = Path("learning_python.txt")

contenido = path.read_text()
lineas = contenido.splitlines()

for linea in lineas:
    nueva_linea = linea.replace("Python", "C++")
    print(nueva_linea)
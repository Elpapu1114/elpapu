from pathlib import Path

path = Path("guest_book.txt")

nombres = ""

while True:
    nombre = input("Ingresá tu nombre (o 'salir' para terminar): ")
    
    if nombre.lower() == "salir":
        break
    
    nombres += nombre + "\n"

# Escribir todos los nombres en el archivo
path.write_text(nombres)

print("Nombres guardados en guest_book.txt")
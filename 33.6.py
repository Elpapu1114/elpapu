archivos = ["gatos.txt", "perros.txt"]

for archivo in archivos:
    try:
        with open(archivo, "r") as f:
            print(f"\nContenido de {archivo}:")
            print(f.read())
    except FileNotFoundError:
        pass  
lugares_favoritos = {
    "rick": ["Paris", "Roma", "Tokio"],
    "Jeffrey": ["Barcelona", "New York"],
    "Papu": ["Mendoza", "Bariloche", "Salta"]
}

for nombre, lugares in lugares_favoritos.items():
    print(f"{nombre} le gusta:")
    for lugar in lugares:
        print(f" - {lugar}")
    print()
frutas_favoritas = ["melocoton", "cerezas", "manzana"]

usuario = []
usuario.append(input("Decime tu fruta 1: ").lower())
usuario.append(input("Decime tu fruta 2: ").lower())
usuario.append(input("Decime tu fruta 3: ").lower())

for fruta in usuario:
    if fruta in frutas_favoritas:
        print(f"¡Te gusta la {fruta} como a mí! :)")
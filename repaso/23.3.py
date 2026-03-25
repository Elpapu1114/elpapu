def hacer_album(artista, titulo):
    return {"artista": artista, "titulo": titulo}

while True:
    print("Ingresá un álbum (o 'salir')")
    
    artista = input("Artista: ")
    if artista == "salir":
        break
    
    titulo = input("Título: ")
    if titulo == "salir":
        break
    
    print(hacer_album(artista, titulo))
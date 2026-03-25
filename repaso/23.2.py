def hacer_album(artista, titulo, canciones=None):
    album = {
        "artista": artista,
        "titulo": titulo
    }
    
    if canciones:
        album["canciones"] = canciones
    
    return album

print(hacer_album("Bad Bunny", "YHLQMDLG"))
print(hacer_album("Duki", "Desde el Fin del Mundo"))
print(hacer_album("Trueno", "Bien o Mal", canciones=13))
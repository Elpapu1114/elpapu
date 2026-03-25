respuestas = {}

while True:
    nombre = input("¿Cómo te llamás? ")
    destino = input("Si pudieras visitar un lugar en el mundo, ¿a dónde irías? ")
    
    respuestas[nombre] = destino
    
    repetir = input("¿Hay otra persona que quiera responder? (si/no): ")
    if repetir.lower() != "si":
        break

print("\nResultados de la encuesta ")
for nombre, destino in respuestas.items():
    print(f"{nombre} quiere ir a {destino}.")
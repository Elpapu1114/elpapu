from pathlib import Path

path = Path("pi_millon.txt")  
contenido = path.read_text()

pi = contenido.replace("\n", "")

cumple = input("Ingresá tu cumpleaños (ddmmaa): ")

if cumple in pi:
    print("🎉 ¡Tu cumpleaños aparece en los primeros un millón de dígitos de pi!")
else:
    print("😢 Tu cumpleaños no aparece.")
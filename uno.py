def main():
    nombrebien =uno()
    dos(nombrebien)

def uno():
    nombre = input("Ingrese su nombre: ")
    nombrebien = nombre.capitalize()
    if nombre.isalnum():
        return nombrebien
    else:
        exit(0)

def dos(nombrebien):
    print("tu nombre es: ", nombrebien)

main()
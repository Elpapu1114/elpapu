edad = int(input("Decime tu edad: "))

if edad < 2:
    print("Es un bebé")
elif edad < 4:
    print("Es un nene chiquito")
elif edad < 13:
    print("Es un nene")
elif edad < 20:
    print("Es un adolescente")
elif edad < 65:
    print("Es un adulto")
else:
    print("Es un adulto mayor")
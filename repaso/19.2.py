while True:
    edad = input("Ingresá tu edad : ")
 
    edad = int(edad)
    
    if edad < 3:
        print("La entrada es gratis.")
    elif edad <= 12:
        print("La entrada cuesta $10.")
    else:
        print("La entrada cuesta $15.")
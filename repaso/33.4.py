while True:
    try:
        num1 = input("Ingresá el primer número (o 'salir'): ")
        if num1.lower() == "salir":
            break
        
        num2 = input("Ingresá el segundo número (o 'salir'): ")
        if num2.lower() == "salir":
            break
        
        num1 = int(num1)
        num2 = int(num2)
        
        print(f"La suma es: {num1 + num2}")
    
    except ValueError:
        print("Error: ingresá solo números.")
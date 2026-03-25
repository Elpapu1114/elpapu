try:
    num1 = int(input("Ingresá el primer número: "))
    num2 = int(input("Ingresá el segundo número: "))
    
    resultado = num1 + num2
    print(f"La suma es: {resultado}")

except ValueError:
    print("Error: tenés que ingresar números válidos.")
ingrediente = ""

while ingrediente.lower() != "salir":
    ingrediente = input("Ingresá un ingrediente (o 'salir'): ")
    
    if ingrediente.lower() != "salir":
        print(f"Voy a agregar {ingrediente} a tu pizza.")

print("¡Pedido terminado!")
while True:
    ingrediente = input("Ingresá un ingrediente (o 'salir'): ")
    
    if ingrediente.lower() == "salir":
        print("¡Pedido terminado!")
        break
    
    print(f"Voy a agregar {ingrediente} a tu pizza.")
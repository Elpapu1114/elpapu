while True:
    ingrediente = input("Ingresá un ingrediente para la pizza (o escribí 'salir' para terminar): ")
    
    if ingrediente.lower() == "salir":
        print("¡Pedido terminado!")
        break
    else:
        print(f"Voy a agregar {ingrediente} a tu pizza.")
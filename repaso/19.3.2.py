activo = True

while activo:
    ingrediente = input("Ingresá un ingrediente (o 'salir'): ")
    
    if ingrediente.lower() == "salir":
        activo = False
    else:
        print(f"Voy a agregar {ingrediente} a tu pizza.")

print("¡Pedido terminado!")
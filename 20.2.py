pedidos_sandwiches = ["jamón y queso", "pastrón", "atún", "pastrón", "aceitunas", "pastrón", "salame y queso"]
sandwiches_terminados = []

print("Lo sentimos, nos quedamos sin pastrón.\n")

# Eliminar todos los "pastrón"
while "pastrón" in pedidos_sandwiches:
    pedidos_sandwiches.remove("pastrón")

# Preparar los demás sándwiches
while pedidos_sandwiches:
    sandwich = pedidos_sandwiches.pop(0)
    print(f"Preparé tu sándwich de {sandwich}.")
    sandwiches_terminados.append(sandwich)

print("\nSándwiches preparados:")
for s in sandwiches_terminados:
    print(f"- {s}")
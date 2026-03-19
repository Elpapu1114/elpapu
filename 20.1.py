pedidos_sandwiches = ["jamón y queso", "atún", "aceitunas", "salame y queso"]
sandwiches_terminados = []

while pedidos_sandwiches:
    sandwich = pedidos_sandwiches.pop(0)
    print(f"Preparé tu sándwich de {sandwich}.")
    sandwiches_terminados.append(sandwich)

print("\nSándwiches preparados:")
for s in sandwiches_terminados:
    print(f"- {s}")
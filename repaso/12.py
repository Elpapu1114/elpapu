pizzas = ["muzzarella", "provolone", "cangrejo"]

pizzas_amigo = pizzas[:]

pizzas.append("fugazzeta")
pizzas_amigo.append("anchoas")

print("Mis pizzas favoritas son:")
for pizza in pizzas:
    print(pizza)

print("Las pizzas favoritas de mi amigos son:")
for pizza in pizzas_amigo:
    print(pizza)
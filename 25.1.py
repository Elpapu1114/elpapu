def hacer_sandwich(*ingredientes):
    print("Sándwich con:")
    for i in ingredientes:
        print(f"- {i}")

hacer_sandwich("jamón")
hacer_sandwich("queso", "tomate")
hacer_sandwich("pollo", "lechuga", "mayonesa")
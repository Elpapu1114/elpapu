class Restaurante:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

class PuestoHelados(Restaurante):
    def __init__(self, nombre, tipo):
        super().__init__(nombre, tipo)
        self.sabores = ["chocolate", "vainilla", "frutilla"]

    def mostrar_sabores(self):
        print("Sabores disponibles:")
        for sabor in self.sabores:
            print(f"- {sabor}")


heladeria = PuestoHelados("Freddo", "Heladería")
heladeria.mostrar_sabores()
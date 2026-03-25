class Restaurant:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def describir_restaurante(self):
        print(f"{self.nombre} es un restaurante de tipo {self.tipo}.")

    def abrir_restaurante(self):
        print("El restaurante está abierto.")
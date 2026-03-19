class Auto:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio


class Bateria:
    def __init__(self, tamano_bateria=40):
        self.tamano_bateria = tamano_bateria

    def describir_bateria(self):
        print(f"La batería es de {self.tamano_bateria} kWh.")

    def obtener_autonomia(self):
        if self.tamano_bateria == 40:
            autonomia = 240
        elif self.tamano_bateria == 65:
            autonomia = 350

        print(f"Este auto puede recorrer aproximadamente {autonomia} km.")

    def actualizar_bateria(self):
        if self.tamano_bateria != 65:
            self.tamano_bateria = 65


class AutoElectrico(Auto):
    def __init__(self, marca, modelo, anio):
        super().__init__(marca, modelo, anio)
        self.bateria = Bateria()


mi_auto = AutoElectrico("Tesla", "Model 3", 2023)

mi_auto.bateria.obtener_autonomia()

mi_auto.bateria.actualizar_bateria()

mi_auto.bateria.obtener_autonomia()
class Restaurante:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
    
    def describir_restaurante(self):
        print(self.nombre, "-", self.tipo)
    
    def abrir_restaurante(self):
        print("El restaurante está abierto")

r = Restaurante("Lo de Jeffrey", "Parrilla")
print(r.nombre)
print(r.tipo)
r.describir_restaurante()
r.abrir_restaurante()
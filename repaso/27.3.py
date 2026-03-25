class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def describir_usuario(self):
        print(self.nombre, self.apellido)
    
    def saludar_usuario(self):
        print(f"Hola {self.nombre}")

u1 = Usuario("Juan", "Perez")
u2 = Usuario("Ana", "Lopez")

u1.describir_usuario()
u1.saludar_usuario()

u2.describir_usuario()
u2.saludar_usuario()
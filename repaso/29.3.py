class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Privilegios:
    def __init__(self):
        self.privilegios = [
            "puede agregar publicaciones",
            "puede eliminar publicaciones",
            "puede bloquear usuarios"
        ]

    def mostrar_privilegios(self):
        print("Privilegios del administrador:")
        for p in self.privilegios:
            print(f"- {p}")


class Administrador(Usuario):
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido)
        self.privilegios = Privilegios()  


admin = Administrador("Guillermo", "Dias")

admin.privilegios.mostrar_privilegios()
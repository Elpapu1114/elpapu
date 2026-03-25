from user import User

class Privileges:
    def __init__(self):
        self.privilegios = [
            "puede agregar publicaciones",
            "puede eliminar publicaciones",
            "puede bloquear usuarios"
        ]

    def show_privileges(self):
        print("Privilegios del administrador:")
        for p in self.privilegios:
            print(f"- {p}")


class Admin(User):
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido)
        self.privileges = Privileges()
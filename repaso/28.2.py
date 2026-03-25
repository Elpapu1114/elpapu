class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.intentos_login = 0
    
    def incrementar_intentos_login(self):
        self.intentos_login += 1
    
    def reiniciar_intentos_login(self):
        self.intentos_login = 0

u = Usuario("Juan")

u.incrementar_intentos_login()
u.incrementar_intentos_login()
print(u.intentos_login)

u.reiniciar_intentos_login()
print(u.intentos_login)
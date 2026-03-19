class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.clientes_atendidos = 0
    
    def establecer_clientes_atendidos(self, n):
        self.clientes_atendidos = n
    
    def incrementar_clientes_atendidos(self, n):
        self.clientes_atendidos += n

r = Restaurante("Lo de Juan")
print(r.clientes_atendidos)

r.establecer_clientes_atendidos(10)
print(r.clientes_atendidos)

r.incrementar_clientes_atendidos(5)
print(r.clientes_atendidos)
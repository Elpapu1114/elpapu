def imprimir_modelos(disenos, completados):
    while disenos:
        d = disenos.pop()
        completados.append(d)

def mostrar_modelos_completados(completados):
    for c in completados:
        print(c)
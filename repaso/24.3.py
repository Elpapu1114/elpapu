def enviar_mensajes(mensajes, enviados):
    while mensajes:
        m = mensajes.pop(0)
        enviados.append(m)

mensajes = ["Hola", "Mensaje 2", "Mensaje 3"]
enviados = []

enviar_mensajes(mensajes[:], enviados)

print("Original:", mensajes)
print("Enviados:", enviados)
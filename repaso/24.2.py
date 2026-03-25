def enviar_mensajes(mensajes, enviados):
    while mensajes:
        m = mensajes.pop(0)
        print(f"Enviando: {m}")
        enviados.append(m)

mensajes = ["Hola", "¿Cómo estás?", "Chau"]
enviados = []

enviar_mensajes(mensajes, enviados)

print("Mensajes:", mensajes)
print("Enviados:", enviados)
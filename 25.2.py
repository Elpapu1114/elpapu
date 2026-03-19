def construir_perfil(nombre, apellido, **info):
    info["nombre"] = nombre
    info["apellido"] = apellido
    return info

perfil = construir_perfil(
    "Guillermo",
    "Dias",
    edad=16,
    ciudad="Buenos Aires",
    hobby="programar"
)

print(perfil)
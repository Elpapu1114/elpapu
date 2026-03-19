def hacer_auto(marca, modelo, **info):
    auto = {
        "marca": marca,
        "modelo": modelo
    }
    auto.update(info)
    return auto

mi_auto = hacer_auto("Toyota", "Corolla", color="gris", airbags=True)
print(mi_auto)
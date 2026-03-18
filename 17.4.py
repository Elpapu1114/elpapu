ciudades = {
    "Buenos Aires": {
        "pais": "Argentina",
        "poblacion": "3 millones",
        "dato": "Es la capital del país"
    },
    "Paris": {
        "pais": "Francia",
        "poblacion": "2 millones",
        "dato": "Tiene la Torre Eiffel"
    },
    "Tokio": {
        "pais": "Japón",
        "poblacion": "14 millones",
        "dato": "Es una de las ciudades más pobladas del mundo"
    }
}

for ciudad, info in ciudades.items():
    print(f"Ciudad: {ciudad}")
    print(f" País: {info['pais']}")
    print(f" Población: {info['poblacion']}")
    print(f" Dato: {info['dato']}\n")
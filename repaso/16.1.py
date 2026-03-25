glosario = {
    "variable": "Es un espacio en la memoria donde se guarda un dato.",
    "lista": "Es una colección de elementos que se pueden modificar.",
    "diccionario": "Es una colección de pares clave-valor.",
    "bucle": "Es una estructura que permite repetir acciones varias veces.",
    "condicional": "Es una estructura que permite tomar decisiones en el programa.",
    "funcion": "Es un bloque de código reutilizable que realiza una tarea.",
    "string": "Es una cadena de texto.",
    "entero": "Es un número sin decimales.",
    "booleano": "Es un valor verdadero o falso.",
    "comentario": "Es texto en el código que no se ejecuta y sirve para explicar."
}

for palabra, definicion in glosario.items():
    print(f"{palabra}:\n  {definicion}\n")
"""
Dado el siguiente diccionario obtener el valor de la "clave1" utilizando el metodo get y
guardarlo en la variable clave1
"""

diccionario = {
    "clave1": 234,
    "clave2": True,
    "clave3": "Valor 1",
    "clave4": [1, 2, 3, 4],
}

clave1 = diccionario.get("clave1", "La clave no existe")
print(clave1)

assert clave1 == 234
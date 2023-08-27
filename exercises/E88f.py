"""
Dado el siguiente diccionario obtener una lista de todas sus valores por medio del método values
"""

diccionario_4 = {
    "clave1": 1234,
    "clave2": 4567,
    "clave3": 8910,
    "clave4": 1112,
}


values = list(diccionario_4.values())
print(values)

assert values == [1234, 4567, 8910, 1112]



"""
Dado el siguiente diccionario obtener una lista de todas sus claves por medio del método keys
"""

diccionario_3 = {
    "clave1": 1234,
    "clave2": True,
    "clave3": "Valor 1",
    "clave4": [1, 2, 3, 4],
}
keys = []

keys = list(diccionario_3.keys())
print(keys)
assert keys == ["clave1", "clave2", "clave3", "clave4"]

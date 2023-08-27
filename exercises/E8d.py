"""
Dado el siguiente diccionario forzar la obtención de un valor por defecto igual a 5 utilizando
el metodo get y almacenarlo en la variable clave5
Restricción: Se debe intentar obtener un valor para la clave inexistente "clave5"
"""

diccionario_2 = {
    "clave1": 234567,
    "clave2": False,
    "clave3": "Valor 13",
    "clave4": [1, 2, 3, 4, 5, 6],
}

clave5 = diccionario_2.get("clave5", 5)
print(clave5)

assert clave5 == 5

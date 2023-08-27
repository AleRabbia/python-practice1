"""
Dado el siguiente diccionario obtener una lista de sus claves y sus valores uno a continuación
de otro por medio del metodo items
"""

diccionario_5 = {
    1: 1111,
    2: 2222,
    3: 3333,
    4: 4444,
}

items = list(diccionario_5.items())
print(items)

assert items == [(1, 1111), (2, 2222), (3, 3333), (4, 4444)]


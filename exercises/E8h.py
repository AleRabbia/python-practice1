"""
Dados dos diccionarios actualizar el primero con los valores del segundo utilizando el método update
"""

diccionario_6 = {
    1: 1111,
    2: 2222,
    3: 3333,
    4: 4444,
}

diccionario_7 = {
    2: 2223,
    3: 3334,
    5: 5555,
    6: 6666,
}

diccionario_6.update(diccionario_7)
print(diccionario_6)
assert diccionario_6 == {1: 1111, 2: 2223, 3: 3334, 4: 4444, 5: 5555, 6: 6666}
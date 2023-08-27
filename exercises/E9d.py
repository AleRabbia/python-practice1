"""
Dados dos conjuntos calcular su interseccion utiilizando el metodo intersection
"""

conjunto_03 = {1, 23, 4, 8, 5, 10, 15, 21}
conjunto_04 = {12, 4, 10, 21, 78}

conjunto_interseccion = conjunto_03.intersection(conjunto_04)
print(conjunto_interseccion)

assert conjunto_interseccion == {10, 4, 21}
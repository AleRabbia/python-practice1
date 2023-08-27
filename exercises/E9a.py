"""Conjuntos"""


"""
Inicializar un conjunto vacío y agregarle los valores de las siguiente variables
Restricción: Utilizar el metodo add
"""

numero_1 = 1
numero_2 = 2
numero_3 = 3

conjunto_1 = set()

conjunto_1.add(numero_1)
conjunto_1.add(numero_2)
conjunto_1.add(numero_3)

print(conjunto_1)

assert conjunto_1 == {1, 2, 3}

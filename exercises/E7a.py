""""Tuplas y Desempaquetado"""


"""
A partir de ls siguiente lista instanciar una tupla que contenga todos sus valores
y en el mismo orden.
"""

lista = ["casa", "perro", "pato", "gato"]

tupla = tuple(lista)
print(tupla)
assert tupla == ("casa", "perro", "pato", "gato")


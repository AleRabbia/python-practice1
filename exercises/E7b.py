
"""
A partir de ls siguiente tupla instanciar una lista que contenga todos sus valores
y en el mismo orden.
"""

tupla = "casa", "perro", "pato", "gato", "tenedor"

lista = list(tupla)

print(lista)

assert lista == ["casa", "perro", "pato", "gato", "tenedor"]
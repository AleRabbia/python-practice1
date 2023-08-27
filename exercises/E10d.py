"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_04
"""

lista_de_compras = "No comprar nada" and ["Pan", "Aceite", "Sal"]

variable_04 = bool(lista_de_compras)
print(variable_04)

assert variable_04 is True

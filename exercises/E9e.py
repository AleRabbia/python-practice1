"""
Dados dos conjuntos calcular su union utiilizando el caracter pipe
"""

conjunto_05 = {1, 2, 3, 4}
conjunto_06 = {5, 6, 7, 8}

conjunto_union = conjunto_05 | conjunto_06
print(conjunto_union)

assert conjunto_union == {1, 2, 3, 4, 5, 6, 7, 8}


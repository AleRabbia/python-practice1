"""
Dados dos conjuntos calcular su diferencia utiilizando el caracter menos
"""

conjunto_07 = {1, 2, 3, 4, 5, 6, 7, 8}
conjunto_08 = {2, 4, 6, 8}

conjunto_diferencia = conjunto_07 - conjunto_08
print(conjunto_diferencia)

assert conjunto_diferencia == {1, 3, 5, 7}


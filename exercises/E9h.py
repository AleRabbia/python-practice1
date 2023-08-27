"""
Dados dos conjuntos calcular su diferencia diferencia simetrica utiilizando el caracter circunflejo
"""

conjunto_09 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
conjunto_10 = {1, 2, 3, 5, 6, 7, 8}

conjunto_diferencia_simetrica = conjunto_09 ^ conjunto_10
print(conjunto_diferencia_simetrica)

assert conjunto_diferencia_simetrica == {4, 9}


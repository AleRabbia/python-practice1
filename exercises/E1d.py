
"""
Determinar si el número de la variable es divisible por 7.
Restricción: Usar el operador módulo.
"""

numero_incalculable = 2 ** 54 - 1
es_divisible_por_siete = (numero_incalculable % 7) == 0
print (es_divisible_por_siete)
assert es_divisible_por_siete
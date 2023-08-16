
"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si el área es mayor a 5.
Restricción: Usar NOT.
"""

lado_cuadrado = 5
area_cuadrado = pow(lado_cuadrado, 2)

area_mayor_a_cinco = not (area_cuadrado <= 5)
print(area_mayor_a_cinco)

assert area_mayor_a_cinco
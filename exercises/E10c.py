"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_03
"""

Domicilio = "Alsina 2446" or "Pueyrredón y la vía"

variable_03 = bool(Domicilio)
print(variable_03)

assert variable_03 is True

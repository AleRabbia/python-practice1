"""
Interpretar como booleano la siguente variable y guardar el valor resultante en variable_06
"""

diccionario = {} and {"Nombre": "Alberto Paz", "DNI": 12365855}

variable_06 = bool(diccionario)
print(variable_06)

assert variable_06 is False
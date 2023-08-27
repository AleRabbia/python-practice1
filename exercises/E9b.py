"""
Inicializar un conjunto vacío con los valores "5", "6" y "7" y agregarle los valores de
las siguiente variables
Restricción: Utilizar el metodo add
"""

nombre = "Esteban"
domicilio = "Los sauces 3446"
edad = "35"

conjunto_2 = set()
conjunto_2 ={"5", "6" , "7"}

conjunto_2.add(edad)
conjunto_2.add(nombre)
conjunto_2.add(domicilio)
print(conjunto_2)
assert conjunto_2 == {"35", "Esteban", "7", "6", "Los sauces 3446", "5"}


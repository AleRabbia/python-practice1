"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si un auto no es de marca Ford y su modelo es igual o anterior al año 2000.
Aclaración: Se puede utilizar and, or y not.
"""

marca_del_auto = "Chevrolet"
modelo_de_auto = 1998

comparar_marca_y_modelo = marca_del_auto != "Ford" and modelo_de_auto <= 2000
print(comparar_marca_y_modelo)


assert comparar_marca_y_modelo


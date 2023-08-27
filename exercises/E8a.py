"""Diccionarios"""


"""
Definir un diccionario para un 'Cliente' que contenga los siguiente valores:
- Clave "Nombre", valor de tipo string: "Mario Pedernera"
- Clave "DNI", valor de tipo integer: 56895632
- Clave "Domicilio", valor de tipo string: Los alamos 4509"
- Clave "Compras", valor de tipo lista: ["cafetera", "TV 50 pulgadas", "mouse gamer"]

"""

Cliente = {'Nombre': 'Mario Pedernera', 'DNI': 56895632, 'Domicilio': "Los alamos 4509", 'Compras': ["cafetera", "TV 50 pulgadas", "mouse gamer"]}

print(Cliente['Nombre'])

assert (
    (Cliente["Nombre"] == "Mario Pedernera")
    and (Cliente["DNI"] == 56895632)
    and (Cliente["Domicilio"] == "Los alamos 4509")
    and (Cliente["Compras"] == ["cafetera", "TV 50 pulgadas", "mouse gamer"])
)

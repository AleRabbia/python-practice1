"""
Desempaquetar la siguiente tupla en las variables a, b y c
"""

tupla = ("primer", 25, [1, 2, 3])

a, b, c = tupla

print(a, b, c)

assert a == "primer" and b == 25 and c == [1, 2, 3]

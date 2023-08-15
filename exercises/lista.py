variables = ['x','y','z']
variables_fun = ['x','y','z']
print(variables)
elemento_eliminado = variables.pop(1)
variables_fun.remove(elemento_eliminado)
print(variables_fun)
print("Se elimino correctamente el elemento ", elemento_eliminado)

print("Se elimino correctamente el elemento ", variables_fun.pop(0))
del variables[1]

print(variables_fun)

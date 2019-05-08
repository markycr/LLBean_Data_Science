# Esto es un comentario
print('Hola Mundo\n')
'''
Esto tambien es un comentario tambien
'''
print('Hola Mundo otra vez\n')

# Ejercicio
# Escribir texto para que se muetre en tres lineas
print('Hola\nMundo\notra vez\n')

#asiganar variables
mi_variable = 10
print(id(mi_variable))
print(mi_variable)

mi_variable = '10'
print(id(mi_variable))
print(mi_variable)

x = 3

print("- Tipo de x:")
print(type(x)) # Imprime el tipo (o `clase`) de x
print("- Valor de x:")
print(x)       # Imprimir un valor
print("- x+1:")
print(x + 1)   # Suma: imprime "4"
print("- x-1:")
print(x - 1)   # Resta; imprime "2"
print("- x*2:")
print(x * 2)   # Multiplicación; imprime "6"
print("- x^2:")
print(x ** 2)  # Exponenciación; imprime "9"
# Modificación de x
x += 1
print("- x modificado:")
print(x)  # Imprime "4"

x *= 2
print("- x modificado:")
print(x)  # Imprime "8"

print("- Varias cosas en una línea:")
print(1,2,x,5*2) # imprime varias cosas a la vez

print (3 != 5)

a = ['a',2*5,'b',3+5,'testing']
print (a)
print(len(a))
print (a[0:3])
print (a[:])
print (a[0],a[3])
a.append('marky')
print (a[:])
a.append(a[:])
print (a[:])
print(len(a))
a.append(a[1]*a[3])
print (a[:])
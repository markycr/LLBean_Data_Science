# crear tupla con 5 elementos diferentes
mi_tupla = ('Uno',2,'Tres',4,'Cinco')
print(mi_tupla)

mi_tupla = mi_tupla + (6, 'Siete')
print(mi_tupla)

mi_tupla += (8, 'Nueve')
print(mi_tupla)

print(mi_tupla[1:-1])

print('Los elementos pares de la tupla: ', mi_tupla[::2])

print('Los elementos pares de la tupla: ', mi_tupla[1::2])
#Ejercicio 1
mis_valores = [5, 6, 10, 13, 3, 4]
print('EJERCICIO #1 >>> Promedio: ', sum(mis_valores)/len(mis_valores))

#Ejercicio 2
todos = [
[177,145,167,190,140,150,180,130], # grupo 1
[165,176,145,189,170,189,159,190], # grupo 2
[145,136,178,200,123,145,145,134], # grupo 3
[201,110,187,175,156,165,156,135] # grupo 4
]
x = 1
mayor = 0
for x in range(len(todos)):
    if todos[mayor] < todos[x]:
        mayor = x

print('EJERCICIO #2 >>> Grupo que contiene la edad mayor: Grupo #', mayor + 1, todos[mayor])
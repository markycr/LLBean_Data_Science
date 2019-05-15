'''
Escriba un programa que permita crear dos listas de palabras y que, a continuación, escriba las siguientes listas (en las que no debe haber repeticiones):
Lista de palabras que aparecen en las dos listas.
Lista de palabras que aparecen en la primera lista, pero no en la segunda.
Lista de palabras que aparecen en la segunda lista, pero no en la primera.
Nota: Para evitar las repeticiones, el programa deberá empezar eliminando los elementos repetidos en cada lista.
'''

def returnNotMatch (a, b):
    a = set(a)
    b = set (b)
    return [list(a & b), list(a - b), list(b - a)]

mylist = []
n = input("Dígame cuántas palabras tiene la lista 1: ")
n = int(n)
for x in range(n):
    valor = input("Dígame la palabra: ")
    mylist.append(valor)

mylist2 = []
n = input("Dígame cuántas palabras tiene la lista 2: ")
n = int(n)
for x in range(n):
    valor = input("Dígame la palabra: ")
    mylist2.append(valor)

x = returnNotMatch(mylist, mylist2)

print('Lista de palabras que aparecen en las dos listas:', x[0])
print('Lista de palabras que aparecen en la primera lista, pero no en la segunda:', x[1])
print('Lista de palabras que aparecen en la segunda lista, pero no en la primera:', x[2])

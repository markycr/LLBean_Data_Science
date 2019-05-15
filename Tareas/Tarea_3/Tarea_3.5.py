"""
5.Escriba un programa que permita crear dos listas de palabras y que, a continuación, elimine de la primera lista los nombres de la segunda lista.
"""
lista = []
n = input("Dígame cuántas palabras tiene la lista 1: ")
n = int(n)
for x in range(n):
    valor = input("Dígame la palabra: ")
    lista.append(valor)
print ('La lista 1 creada es: ', lista)

lista2 = []
n = input("Dígame cuántas palabras tiene la lista 2: ")
n = int(n)
for x in range(n):
    valor = input("Dígame la palabra: ")
    lista2.append(valor)
print ('La lista 2 creada es: ', lista2)

for i in lista2:
    if i in lista:
        lista.remove(i)

print ('La nueva lista es: ', lista)
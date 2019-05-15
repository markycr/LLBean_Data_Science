"""
6.Escriba un programa que permita crear una lista de palabras y que, a continuación, cree una segunda lista igual a la primera, pero al revés (no se trata de escribir la lista al revés, sino de crear una lista distinta).
"""
lista = []
lista2 = []
n = input("Dígame cuántas palabras tiene la lista 1: ")
n = int(n)
for x in range(n):
    valor = input("Dígame la palabra: ")
    lista.append(valor)
    lista2.insert(0, valor)
print ('La lista 1 creada es: ', lista)
print ('La lista 2 creada es: ', lista2)

"""
2.Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.
"""
lista = []
n = input("Dígame cuántas palabras tiene la lista: ")
n = int(n)
for x in range(n):
    valor = input("Dígame la palabra: ")
    valor = str(valor)
    lista.append(valor)
print ('La lista creada es: ', lista)
buscar = input("Dígame la palabra a buscar: ")
buscar = str(buscar)
result = 0
for x in range(len(lista)):
    result = result + lista[x].count(buscar)
print('La palabra', buscar, 'aparece en la lista la siguiente cantidad de veces:', result)
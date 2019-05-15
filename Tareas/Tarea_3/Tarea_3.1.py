"""
1.Escriba un programa que permita crear una lista de palabras.
Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista.
Por último, el programa tiene que escribir la lista.
"""
lista = []
n = input("Dígame cuántas palabras tiene la lista: ")
n = int(n)
for x in range(n):
    valor = input("Dígame la palabra: ")
    lista.append(valor)
print ('La lista creada es: ', lista)
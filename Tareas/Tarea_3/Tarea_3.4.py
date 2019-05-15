"""
4.Escriba un programa que permita crear una lista de palabras y que, a continuación, pida dos palabras y sustituya la primera por la segunda en la lista.
"""
lista = []
n = input("Dígame cuántas palabras tiene la lista: ")
n = int(n)
for x in range(n):
    valor = input("Dígame la palabra: ")
    lista.append(valor)
print ('La lista creada es: ', lista)
a = input("Dígame la palabra a eliminar: ")
a = str(a)
lista.remove(a)
print ('La nueva lista creada es: ', lista)
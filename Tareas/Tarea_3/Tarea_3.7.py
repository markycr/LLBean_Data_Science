"""
7.Escriba un programa que permita crear una lista de palabras y que, a continuación, elimine los elementos repetidos (dejando únicamente el primero de los elementos repetidos).
"""
mylist = []
n = input("Dígame cuántas palabras tiene la lista 1: ")
n = int(n)
for x in range(n):
    valor = input("Dígame la palabra: ")
    mylist.append(valor)

mylist = list(dict.fromkeys(mylist))
print (mylist)
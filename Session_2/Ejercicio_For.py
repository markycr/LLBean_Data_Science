#Ejercicio: Escribir un for para buscar el máximo de la lista e imprimirlo
lista=[44,11,15,29,53,12,30]
maximo=0
# IMPLEMENTAR
for i in lista:
    if maximo < i:
        maximo = i

# debe imprimir 53
print("- El maximo es:")
print(maximo)

print(max(lista))
print("¿Cual es tu edad?")
Edad = 19
if Edad < 18:
    print('Menor de edad')
else:
    print('Mayor de edad')


#Ejercicio
# Pasar a escala de grises el color codificado en los elementos de la lista `pixel`

pixel= [0.6,0.3,0.4] # intensidades de cada canal.
#El elemento 0 es el R, el 1 el G y el 2 el B

# la intensidad en escala de grises es el promedio de la intensidad de cada canal R, G y B
intensidad = sum(pixel)/len(pixel) # IMPLEMENTAR

print("La intensidad es:")
print(intensidad)

#Ejercicio
# Pasar a blanco y negro el valor de intensidad codificado en la variable intensidad


# podemos considerar que un pixel se convierte en blanco si su intensidad en escala de grises es mayor a 0.5
# y negro de lo contrario
if intensidad > 0.5:
    bw = 'Blanco' # IMPLEMENTAR
else:
    bw = 'Negro'  # IMPLEMENTAR

print("En blanco y negro el pixel sería:")
print(bw)
#Variables
pi = '3.1415926'
asterix = '*'
acumulado = ''

while pi!= '3.1':
    acumulado = acumulado + asterix + ' ' + pi + ' '
    print (asterix + ' ' + pi)
    pi = pi[:len(pi)-1]
    asterix = asterix + '*'

print(acumulado)
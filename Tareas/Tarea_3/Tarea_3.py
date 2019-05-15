# Para definir la agenda del hospital
agenda_hospital = []
persona = ('Juan', 'Mora', 100103111,65 , 81118811, 'dolor')
# agregamos una persona
agenda_hospital.append(persona)
# podemos revisar cual es el estatus de la agenda
print(agenda_hospital)
[('Juan', 'Mora', 100103111, 65, 81118811, 'dolor')]
# viene otra persona
persona = ('Ana', 'Jimenez', 32415116,50 , 46261266, 'consulta')
# agregamos otra persona
agenda_hospital.append(persona)
# podemos revisar cual es el estatus de la agenda
print(agenda_hospital)
[('Juan', 'Mora', 100103111, 65, 81118811, 'dolor'), ('Ana', 'Jimenez', 32415116, 50, 46261266, 'consulta')]
# suponga que vienen 5 personas mas
persona =[('Sofia',   'Alfaro',   32415116,   36 , 51161161, 'consulta'),
          ('Carlos',  'Sanchez',  33411151,   15 , 41655161, 'dolor'),
          ('Felipe',  'Perez',    12243151,   42 , 65151111, 'documento'),
          ('Melissa', 'Alvarado', 734114144,  10 , 87421312, 'dolor'),
          ('Pedro',   'Castro',   4372124141, 2 ,  99313131, 'dolor'),]
# Podemos agregar esas personas que vienen todos de una sola vez
agenda_hospital.extend(persona)
print(agenda_hospital)
[('Juan', 'Mora', 100103111, 65, 81118811, 'dolor'), ('Ana', 'Jimenez', 32415116, 50, 46261266, 'consulta'), ('Sofia', 'Alfaro', 32415116, 36, 51161161, 'consulta'), ('Carlos', 'Sanchez', 33411151, 15, 41655161, 'dolor'), ('Felipe', 'Perez', 12243151, 42, 65151111, 'documento'), ('Melissa', 'Alvarado', 734114144, 10, 87421312, 'dolor'), ('Pedro', 'Castro', 4372124141, 2, 99313131, 'dolor')]
# notemos que la impresión en pantalla está un poco sucia... lo arreglamos
for paciente in agenda_hospital:
    print(paciente)
('Juan', 'Mora', 100103111, 65, 81118811, 'dolor')
('Ana', 'Jimenez', 32415116, 50, 46261266, 'consulta')
('Sofia', 'Alfaro', 32415116, 36, 51161161, 'consulta')
('Carlos', 'Sanchez', 33411151, 15, 41655161, 'dolor')
('Felipe', 'Perez', 12243151, 42, 65151111, 'documento')
('Melissa', 'Alvarado', 734114144, 10, 87421312, 'dolor')
('Pedro', 'Castro', 4372124141, 2, 99313131, 'dolor')

print('\n')
print('PREGUNTA #1 >>> Cuantos pacientes llegaron en total?', 'RESPUESTA: ', len(agenda_hospital), '\n')

x = 0
dolor = 0
for x in range(len(agenda_hospital)):
    dolor = dolor + agenda_hospital[x].count('dolor')
print('PREGUNTA #2 >>> Cuantas personas llegaron por dolor?', 'RESPUESTA: ', dolor, '\n')

#Suponga que se atienden con orden de prioridad por edad, empezando por el adulto mayor.
agenda_hospital.sort(key=lambda x: x[3], reverse=True)
print('PREGUNTA #3 >>> Ordene la lista desde el más adulto al más joven', 'RESPUESTA: ')
for paciente in agenda_hospital:
    print(paciente)

print('\n')
mayores = 0
for x in range(len(agenda_hospital)):
    if agenda_hospital[x][3] > 17:
        mayores = mayores + 1
print('PREGUNTA #4 >>> Cuantos pacientes son mayores de edad? cuantos menores?', 'RESPUESTA: Mayores:', mayores, 'Menores:', len(agenda_hospital)- mayores)

#Suponga que se atienden con orden de prioridad por gravedad de consulta, empezando por los que tienen dolor y luego por edad (mas viejo al joven), empezando por el adulto mayor.
#Ordene la lista empenzando por los que tienen mayor prioridad.
print('\n')
print('PREGUNTA #5 >>> Lista de pacientes ordenados por dolencia y edad:')
agenda_hospital.sort(key=lambda x: (x[5],x[3]), reverse=True)
for paciente in agenda_hospital:
    print(paciente)

#Suponga que los que tienen dolor mueren :( Como queda la lista de pacientes vivos por atender ordenados por orden de edad desde el joven al viejo.
print('\n')
print('PREGUNTA #6 >>> Lista actualizada descartando a pacientes muertos:')
listd = []
for x in agenda_hospital:
    if x[5] == 'dolor':
        listd.append(x)
for x in listd:
    agenda_hospital.remove(x)

agenda_hospital.sort(key=lambda x: x[3], reverse=True)
for paciente in agenda_hospital:
   print(paciente)
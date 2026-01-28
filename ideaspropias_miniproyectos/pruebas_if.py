# Voy a generar varias prruebas o mini ejercicios para practicar el uso de estructuras condicionales if, elif y else en Python.

# Prueba 1 - Vamos a crear un programa que verifique si un número es positivo, negativo o cero.

# Le pedidmos al usuario que meta un numero

numero_usuario = int(input('Introduce un numero: '))

if numero_usuario < 0:
    print(f'El número {numero_usuario} es negativo')
elif numero_usuario > 0:
    print(f'El número {numero_usuario} es positivo')
else:
    print(f'El número introducido es {numero_usuario}')

# --------------------------------------------------------------------------------------------------------------------

# Ahora la siguiente prueba, quiero meter condicional if / elif / else y el uso de and / or / not cualquiera de ellos

# Prueba 2 - Creamos un programa que pida al usuario su edad y si tiene carnet de conducir.
# Con esa información, el programa debe determinar si la persona puede conducir legalmente.

edad = int(input('Pon tu edad: '))
tiene_carnet = input('Tienes carnet de conducir (Si/No)? ')
MAYORIA_EDAD = 18

if edad >= MAYORIA_EDAD and tiene_carnet.strip().lower() == 'si':
    print(f'Tienes {edad} años y carnet de conducir, por lo que legalmente puedes conducir.')
elif edad >= MAYORIA_EDAD and  not (tiene_carnet.strip().lower() == 'si'):
    print(f'Eres mayor de edad, pero no tines carnet. Legalmente no puedes conducir.')
elif edad < MAYORIA_EDAD:
    print(f'Tines {edad} años eres menor de edad, no puedes conducir.')
else:
    print('Datos no validos.')

# --------------------------------------------------------------------------------------------------------------------

# Prueba 3 - Crear un programa que pida al usuario un número y determine si es par o impar.

print('*** Par o Impar ***')
numero_usuario1 = int(input('\nIntroduce el numero: '))
numero_par = numero_usuario1 % 2 == 0

if numero_par:
    print(f'El número {numero_usuario1} es par.')
else:
    print(f'El número {numero_usuario1} no es par.')


# --------------------------------------------------------------------------------------------------------------------
# Prueba 4 - Crear un programa que pida al usuario su calificación en un examen y determine si ha aprobado o no.

print('*** Aprobado o No Aprobado ***')
calificacion_examen = float(input('Introduce tu nota del examen (Del 0 al 10): '))

if calificacion_examen >= 5 and calificacion_examen < 7:
    print(f'Enhorabuena, con un {calificacion_examen:.2f} tienes un Suficiente')
elif calificacion_examen >= 7 and calificacion_examen < 9:
    print(f'Enhorabuena, con un {calificacion_examen:.2f} tienes un Notable')
elif calificacion_examen >= 9 and calificacion_examen <= 10:
    print(f'Enhorabuena, con un {calificacion_examen:.2f} tienes un Sobresaliente')
elif calificacion_examen < 5:
    print(f'Mas suerte la próxima, con un {calificacion_examen:.2f} tienes un Suspenso')
else:
    print('Introduce un valor correcto.')
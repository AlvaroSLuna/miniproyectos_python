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


# --------------------------------------------------------------------------------------------------------------------

# Prueba 5 - Creamos un programa que le pida una contraseña y la valide. El programa debe seguir pidiendola hasta que sea correcta

pswd_real = 'Python123'
pswd_usuario = ''

# Bucle que sigue pidiendo la contraseña hasta que sea correcta
while pswd_usuario != pswd_real:
    pswd_usuario = input('Introduce la contraseña: ')
    
    if pswd_usuario != pswd_real:
        print('Contraseña Incorrecta.')
print('Contraseña Correcta.')


# --------------------------------------------------------------------------------------------------------------------

# Prueba 6 - Crear un programa que pida al usuario un número del 1 al 7 y devuelva el día de la semana correspondiente.

print('*** Día de la Semana ***')
numero_dia = int(input('Introduce un número del 1 al 7: '))

if numero_dia == 1:
    print(f'El día {numero_dia} es el Lunes')
elif numero_dia == 2:
    print(f'El día {numero_dia} es el Martes')
elif numero_dia == 3:
    print(f'El día {numero_dia} es el Miercoles')
elif numero_dia == 4:
    print(f'El día {numero_dia} es el Jueves')
elif numero_dia == 5:
    print(f'El día {numero_dia} es el Viernes')
elif numero_dia == 6:
    print(f'El día {numero_dia} es el Sábado')
elif numero_dia == 7:
    print(f'El día {numero_dia} es el Domingo')
else:
    print('Introduce un valor valido')


# --------------------------------------------------------------------------------------------------------------------

# Prueba 7 - Crear un programa que pida al usuario su altura en cm y determine si es apto para montar en una atracción de parque de diversiones (altura mínima 120 cm).
print('*** Altura para Atracción ***')

ALTURA_MINIMA = 120
altura_usuario = (int(input('Introduce tu altura en centimetros para ver si puedes subir: ')))

if altura_usuario >= ALTURA_MINIMA:
    print(f'Enhorabuena tu altura es de {altura_usuario} cm por lo que puedes montar en la atracción.')
elif altura_usuario < ALTURA_MINIMA:
    print(f'Tu altura es de {altura_usuario} cm no cumples con la altura minima necesaria para subir a la atracción que es de {ALTURA_MINIMA} cm')
else:
    print('Introduce un valor correcto.')


# --------------------------------------------------------------------------------------------------------------------

# Prueba 8 - Crear un programa que pida al usuario un año y determine si es bisiesto o no.
print('*** Año Bisiesto ***')
anio_usuario = int(input('Introduce un año para ver si es bisiesto: '))

if (anio_usuario % 4 == 0 and anio_usuario % 100 != 0) or (anio_usuario % 400 == 0):
    print(f'El año {anio_usuario} es bisiesto.')
elif anio_usuario % 4 != 0 or (anio_usuario % 100 == 0 and anio_usuario % 400 != 0):
    print(f'El año {anio_usuario} no es bisiesto.')
else:
    print('Introduce un valor correcto.')


# --------------------------------------------------------------------------------------------------------------------

# Prueba 9 - Vamos a crear un programa que pida al usuario tres números y determine cuál es el mayor.

print('*** Número Mayor ***')
num1 = int(input('Introduce el primer número: '))
num2 = int(input('Introduce el segundo número: '))
num3 = int(input('Introduce el tercer número: '))

if num1 > num2 and num1 > num3:
    print(f'El numero mayor es: {num1}')
elif num2 > num1 and num2 > num3:
    print(f'El numero mayor es: {num2}')
elif num3 > num1 and num3 > num2:
    print(f'El numero mayor es: {num3}')
else:
    print('Al menos dos números deben ser distintos entre sí')


# --------------------------------------------------------------------------------------------------------------------
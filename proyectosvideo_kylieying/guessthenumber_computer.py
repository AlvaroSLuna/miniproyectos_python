# Efectivamente, quiero probar a hacer funciones sin antes haberlas visto en el curso.
# Creo que voy a intentar hacer un programa en la cual al maquina genere numeros aleatorios
# y yo debo de adivinar si el numero es mayor o menor con varios intentos.

# Por lo que veo en el video que estoy usando de guia, vamos a usar while, osea bucles.

# def es una palabra reservada para definir funciones en python.

from random import randint

def guess(x):
    random_number = randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Adivina un numero entre 1 y {x}: '))
        if guess < random_number:
            print('Lo siento, intenta de nuevo. El numero es muy bajo.')
        elif guess > random_number:
            print('Lo siento, intenta de nuevo. El numero es muy alto.') 
    print(f'Felicidades! Adivinaste el numero {random_number} correctamente!')
    
guess(10)
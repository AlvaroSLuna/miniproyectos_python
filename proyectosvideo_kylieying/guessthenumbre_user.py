# Vamos a hacer como en el ejercicio de que el usuario adivine el numero que la computadora genera aleatoriamente, pero al reves.
# La computadora intentara adivinar el numero que el usuario piensa, y el usuario le dira si es mayor o menor.

from random import randint

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c': # 'c' para correcto y evitar bucle infinito
        guess = randint(low, high)
        feedback = input(f'Mi suposicion es {guess}. Si es muy bajo, escribe "b". Si es muy alto, escribe "a". Si es correcto, escribe "c": ').lower()
        if feedback == 'a':
            high = guess - 1
        elif feedback == 'b':
            low = guess + 1
    print(f'Yay! El ordenador adivino tu numero {guess} correctamente!')

computer_guess(100)
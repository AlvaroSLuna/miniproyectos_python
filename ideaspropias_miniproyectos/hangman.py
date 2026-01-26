# Vamos a crear un juego simple de "Ahorcado" en Python.
# El objetivo del juego es adivinar una palabra oculta letra por letra antes de quedarse sin intentos.

import random

# Creamos una lista de palabras para poder usar en el juego
palabras = ['Tomate', 'Azucar', 'Sal', 'Juegos', 'Agua', 'Movil', 'Televisor', 'Python']

# Creamos una función que escoge de manera aleatoria una palabra de nuestra lista
def obtener_palabra(palabras):
    return random.choice(palabras).lower()

# Esta es la función principal
def ahorcado():
    # Presentamos el juego al usuario
    print('===================================')
    print(' Bienvenido al juego del Ahorcado')
    print('===================================')

    # Creamos las variables necesarias
    palabra = obtener_palabra(palabras)
    # Representa el progreso del jugador con guiones bajos, por cada letra no adivinada.
    progreso = ['_' for _ in palabra]
    # Conjunto para llevar un registro de las letras ya usadas
    letras_usadas = set()
    fallos = 0
    max_fallos = 6 

    # Bucle principal del juego. El juego continúa hasta que el jugador adivine la palabra o se quede sin intentos.
    while fallos < max_fallos and '_' in progreso:
        # Mostramos el progreso actual y las letras usadas
        print("\nPalabra:", " ".join(progreso))
        print("Letras usadas:", ", ".join(sorted(letras_usadas)))
        print(f"Fallos: {fallos}/{max_fallos}\n")

        # Pedimos al usuario que introduzca una letra
        letra = input("Introduce una letra: ").lower()
        # Si la entrada no es válida, pedimos otra letra
        if len(letra) != 1 or not letra.isalpha():
            print("\nIntroduce solo una letra válida.")
            continue
        # Si la letra ya ha sido usada, pedimos otra letra
        if letra in letras_usadas:
            print("\n Ya has usado esa letra.")
            continue
        # Añadimos la letra a las letras usadas
        letras_usadas.add(letra)

        # Comprobamos si la letra está en la palabra
        if letra in palabra:
            for i, c in enumerate(palabra):
                if c == letra:
                    progreso[i] = letra
        # Si la letra no está en la palabra, incrementamos el contador de fallos
        else:
            fallos += 1

    # Comprobamos si el jugador ha ganado o perdido. not in es para ver si quedan letras por adivinar
    if '_' not in progreso:
        print("\n¡Has ganado! La palabra era:", palabra)
    else:
        print("\nHas perdido. La palabra era:", palabra)

# Ejecutamos el juego
ahorcado()
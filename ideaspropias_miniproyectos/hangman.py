# Vamos a crear un juego simple de "Ahorcado" en Python.
# El objetivo del juego es adivinar una palabra oculta letra por letra antes de quedarse sin intentos.

import random

# Creamos una lista de palabras para poder usar en el juego
palabras = ['Tomate', 'Azucar', 'Sal', 'Juegos', 'Agua', 'Movil', 'Televisor', 'Python']

# Creamos una función que escoge de manera aleatoria una palabra de nuestra lista
def obtener_palabra(palabras):
    return random.choice(palabras).lower()

# Dibujos del ahorcado según los fallos
AHORCADO = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

# Esta es la función principal
def ahorcado():
    # Presentamos el juego al usuario
    print('===================================')
    print(' Bienvenido al juego del Ahorcado')
    print('===================================')

    # Creamos las variables necesarias
    palabra = obtener_palabra(palabras)
    progreso = ['_' for _ in palabra]
    letras_usadas = set()
    fallos = 0
    max_fallos = 6 

    # Bucle principal del juego
    while fallos < max_fallos and '_' in progreso:
        print(AHORCADO[fallos])  # Mostrar dibujo según fallos
        print("Palabra:", " ".join(progreso))
        print("Letras usadas:", ", ".join(sorted(letras_usadas)))
        print(f"Fallos: {fallos}/{max_fallos}\n")

        letra = input("Introduce una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("\nIntroduce solo una letra válida.")
            continue

        if letra in letras_usadas:
            print("\nYa has usado esa letra.")
            continue

        letras_usadas.add(letra)

        if letra in palabra:
            for i, c in enumerate(palabra):
                if c == letra:
                    progreso[i] = letra
        else:
            fallos += 1

    # Final del juego
    print(AHORCADO[fallos])  # Mostrar dibujo final

    if '_' not in progreso:
        print("\n¡Has ganado! La palabra era:", palabra)
    else:
        print("\nHas perdido. La palabra era:", palabra)

# Ejecutamos el juego
ahorcado()
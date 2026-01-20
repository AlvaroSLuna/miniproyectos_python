# Vamos a crear un juego de piedra, papel o tijera contra el ordenador, todo por consola.

from random import choice

def play():
    user = input(f"Elige 'r' para piedra, 'p' para papel o 's' para tijera: \nr").lower()
    computer = choice(['r', 'p', 's'])
    print(f'La computadora eligio: {computer}')

    if user == computer:
        return 'Es un empate!'
    
    if is_win(user, computer):
        return '¡Ganaste!'
    
    return '¡Perdiste!'


def is_win(player, opponent):
    # Devuelve True si el jugador gana
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())    
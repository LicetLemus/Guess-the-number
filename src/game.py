import random

from src.players import player_user, player_computer, number_user, number_computer
from src.utils import validate_number


MAX_TRY = 10

def game():
    """The function allows the players to play the game in the while loop
    that call the functions player_user(), validate_number(), player_computer()
    in base of the try_done_round variable.
    """
    print("Bienvenido al juego de adivinar el número, ¡Buena suerte!")
    number_random = random.randint(1, 100)
    print("¡se ha generado un número aleatorio entre 1 y 100!")

    try_done_round = 0
    while try_done_round < MAX_TRY:
        player_user()
        validate_number(number_user[-1], number_random)
        player_computer(number_random)
        try_done_round += 1

        if try_done_round == 10:
            print("¡Has agotado tus intentos!")
            break
        print("Intentos restantes: ", MAX_TRY - try_done_round)
    print("\nEl número a adivinar era: ", number_random)

    # .join () method returns a string in which the elements of sequence have been
    # joined by str separator ' '.
    # .map() function returns a list of the results converted to string
    print("numeros introducidos por el usuario:", ' '.join(map(str, number_user)))
    print("numeros introducido por el ordenador:",' '.join(map(str, number_computer)))
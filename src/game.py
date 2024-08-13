import random

from .players import get_number_user, get_number_computer, print_number_user_computer
from .utils import get_random_number, validate_number, print_information

MAX_TRY = 10

def game():
    """ The function allows the user to play the game.
    """
    number_random = get_random_number(1, 100)
    print_information()

    try_done_round = 0
    while try_done_round < MAX_TRY:
        number_user = get_number_user()
        number_computer = get_number_computer(number_user,number_random)
        print_number_user_computer(number_user, number_computer)
        
        if validate_number(number_user[-1], number_random, "usuario"):
            print("¡Juego terminado!")
            break
        
        # si el número introducido por el ordenador es igual al número aleatorio en caso de que sea false se sigue con el juego
        if validate_number(number_computer[-1], number_random, "ordenador"):
            print("¡Juego terminado!")
            break
        
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
# The game module contains the game function that allows the user to play the game.
from .players import set_number_user, set_number_computer, print_number_user_computer
from .utils import get_random_number, print_information, get_validate_number

MAX_TRY = 10

def game():
    """
    The function generates a random number between 1 and 100 and asks the user to guess it.
    The user and the computer have a maximum of 10 attempts to guess the number.
    """
    ranges = {
        "min": 1,
        "max": 100
    }
    number_random = get_random_number(ranges)
    print_information()

    numbers_user_computer = []  # Lista para almacenar los números introducidos por ambos
    feedback_list = [""]
    
    try_done_round = 0
    
    while try_done_round < MAX_TRY:
        number_user, numbers_user_computer = set_number_user(numbers_user_computer)
        if number_user is None:
            continue  # Si el número no es válido, pedir al usuario que intente de nuevo
        
        
        # Obtener el número de la computadora
        number_computer, numbers_user_computer = set_number_computer(numbers_user_computer, feedback_list[-1], ranges)
        
        #mostrar los numeros de los jugadores
        print_number_user_computer(number_user, number_computer)
        
        is_correct_user, message_user = get_validate_number(number_user, number_random, ranges, "usuario")
        feedback_list.append(message_user)
        print(message_user)
        if is_correct_user:
            print("¡Juego terminado!")
            break
        
        is_correct_computer, message_computer = get_validate_number(number_computer, number_random, ranges, "computadora")
        print(message_computer)
        if is_correct_computer:
            print("¡Juego terminado!")
            break
        
        try_done_round += 1

        if try_done_round == MAX_TRY:
            print("¡Has agotado tus intentos!")
            break
        
        print("Intentos restantes: ", MAX_TRY - try_done_round)
    print("\nEl número a adivinar era: ", number_random)

    # .join () method returns a string in which the elements of sequence have been
    # joined by str separator ' '.
    # .map() function returns a list of the results converted to string

    print("numeros introducidos por el usuario:", ' '.join(map(str, numbers_user_computer[::2]))) # Imprimir los números introducidos por el usuario impares
    print("numeros introducido por el ordenador:",' '.join(map(str, numbers_user_computer[1::2]))) # Imprimir los números introducidos por el ordenador pares
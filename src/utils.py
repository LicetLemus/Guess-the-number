import random

def print_information():
    print("Bienvenido al juego de adivinar el número, ¡Buena suerte!")
    print("¡se ha generado un número aleatorio entre 1 y 100!")

def get_random_number(range_limit):
    """"
    The function generates a random number between 1 and 100.
    
    Args:
        range_limit (tuple): A tuple with the range of numbers to generate the random number.
        
    return : int: The random number generated.
    """
    a, b = range_limit
    number_random = random.randint(a, b)
    return number_random

def get_validate_number(number, number_random, range_limit, entity=""):
    """The function validates the number entered by the user or the computer.  
    Args:
        number (int): The number to validate.
        number_random (int): The number to compare against.
        entity (str): A description of who is guessing (e.g., "usuario" or "ordenador").
    
    Returns:
        bool: True if the number is correct, False otherwise.
        str: A message indicating if the number is correct or not.
    """
    if not number or number < range_limit[0] or number > range_limit[1]:
        return False, f"{entity}: El número no es válido"
    elif number == number_random:
        return True, f"¡Ganaste {entity}!, adivinaste el número"
    elif number < number_random:
        return False, f"{entity}: El número a adivinar es mayor"
    else:
        return False, f"{entity}: El número a adivinar es menor"

    
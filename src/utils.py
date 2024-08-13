import random

def print_information():
    print("Bienvenido al juego de adivinar el número, ¡Buena suerte!")
    print("¡se ha generado un número aleatorio entre 1 y 100!")

def get_random_number(a, b):
    """"
    The function generates a random number between 1 and 100.
    
    Args:
        a : int: The lower limit of the range.
        b : int: The upper limit of the range.
        
    return : int: The random number generated.
    """
    number_random = random.randint(a, b)
    return number_random

def get_validate_number(number, number_random, entity=""):
    """The function validates the number entered by the user or the computer.  
    Args:
        number (int): The number to validate.
        number_random (int): The number to compare against.
        entity (str): A description of who is guessing (e.g., "usuario" or "ordenador").
    
    Returns:
        bool: True if the number is correct, False otherwise.
        str: A message indicating if the number is correct or not.
    """
    if not number or number < 1 or number > 100:
        return False, f"{entity}: El número no es válido"
    elif number == number_random:
        return True, f"¡Ganaste {entity}!, adivinaste el número"
    elif number < number_random:
        return False, f"{entity}: El número a adivinar es mayor"
    else:
        return False, f"{entity}: El número a adivinar es menor"

    
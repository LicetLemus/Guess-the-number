import random

def print_information():
    """
    The function prints a welcome message
    """
    print("Bienvenido al juego de adivinar el número, ¡Buena suerte!")
    print("¡se ha generado un número aleatorio entre 1 y 100!")

def get_random_number(ranges):
    """"
    The function generates a random number.
    
    Args:
        range_limit (tuple): A tuple with the range of numbers to generate the random number.
        
    return : int: The random number generated.
    """
    min = ranges["min"]
    max = ranges["max"]
    number_random = random.randint(min, max)
    return number_random

def get_validate_number(number, number_random, ranges, entity=""):
    """The function validates the number entered by the user or the computer.  
    Args:
        number (int): The number to validate.
        number_random (int): The number to compare against.
        range_limit (tuple): A tuple with the range of numbers to validate the number.
        entity (str): A description of who is guessing (e.g., "usuario" or "ordenador").
    
    Return:
        bool: True if the number is correct, False otherwise.
        str: A message indicating if the number is correct or not.
    """
    print("number------------------------------------", number)
    if number < ranges['min'] or number > ranges['max']:
        return False, f"{entity}: El número no es válido"
    elif number == number_random:
        return True, f"¡Ganaste {entity}!, adivinaste el número"
    elif number < number_random:
        return False, "random es mayor"
    else:
        return False, "random es menor"
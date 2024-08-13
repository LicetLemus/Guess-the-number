def validate_number(number, number_random, entity=""):
    """The function validates the number entered by the user or computer
    and compares it with the random number.
    
    Args:
        number (int): The number to validate.
        number_random (int): The number to compare against.
        entity (str): A description of who is guessing (e.g., "usuario" or "ordenador").
    
    Returns:
        bool: True if the number is correct, False otherwise.
    """
    
    if not number or number < 1 or number > 100:
        print(f"El número introducido no es válido ({entity})")
        return False
    elif number == number_random:
        print(f"¡Felicidades! Has adivinado el número ({entity})")
        return True
    elif number < number_random:
        print(f"El número a adivinar es mayor ({entity})")
        return False
    else:
        print(f"El número a adivinar es menor ({entity})")
        return False

    
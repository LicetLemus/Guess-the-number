import random

numbers_user = []
numbers_computer = []
numbers_user_computer = [] # lista con los números usuario y compu filtrada sin ceros, no repetidos


def get_input_value():
    """
    The function allows the user to enter a number
    
    Args:
        None
        
    Return:
        int: The number entered by the user.
    
    """
    input_value = input("\nIntroduce un número: ")
    return input_value


def validate_number_user(input_value):
    if input_value.isdigit():
        return int(input_value)
    else:
        print("No has introducido un numero válido")
        return 0 # si no es un número, se devuelve 0


def set_number_user():
    """
    This function call the validate_number_user function and add the number entered by the user to a list.
    
    Args:
        None
        
    Return:
        list: The list with the number entered by the user.
    """
    input_value = get_input_value()
    number_user_current = validate_number_user(input_value)
    numbers_user.append(number_user_current)
    return numbers_user
    
#-------------------------------------------------------------computer------------------------------------------------------------
def get_number_computer(feedback):
    """
    The function generates a random number for the computer.
    
    Args:
        number_user (int): The number entered by the user.
    return:
        int: The number generated for the computer.
    """
    last_number_user = numbers_user[-1]
    if feedback == "":
        return random.randint(1, 100)
    if feedback == "random es mayor":
        return random.randint(last_number_user, 100)
    elif feedback == "random es menor":
        return random.randint(1, last_number_user)
    

def set_number_computer(feedback):
    """
    This function call the get_number_computer function and add the number entered by the computer to a list.
    
    Args:
        number_user (int): The number entered by the user.
        
    Return:
        list: The list with the number entered by the computer.
    """
    number_computer_current = get_number_computer(feedback)
    numbers_computer.append(number_computer_current)
    return numbers_computer


def print_number_user_computer(number_user, number_computer):
    """
    The function prints the number entered by the user and the computer.
    """
    print("El usuario ha introducido el número: ", number_user[-1])
    print("El ordenador ha introducido el número: ", number_computer[-1])
    
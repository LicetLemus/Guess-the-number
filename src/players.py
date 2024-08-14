import random

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


def validate_number_user(input_value, ranges):
    """
    This function validates the number entered by the user.
    
    Args:
        input_value (str): The number entered by the user.
        
    Return:
        int: The number entered by the user if it is valid, None otherwise.
    
    """
    if not input_value.isdigit():
        print("El número no es válido. Debe ser un número entero.")
        return None
    
    number_user = int(input_value)
    if not ranges["min"] <= number_user <= ranges["max"]:
        print("El número no es válido. Debe estar entre 1 y 100.")
        return None
    
    return number_user


def set_number_user(user_computer_numbers, ranges):
    """
    This function call the validate_number_user function and add the number entered by the user to a list.
    
    Args:
        user_computer_numbers (list): The list with the numbers entered by the user and the computer
        
    Returns:
        int: The number entered by the user.
        list: The list update with the number entered by the user and the computer.
    """
    input_value = get_input_value()
    number_user = validate_number_user(input_value, ranges)
    if number_user is not None:
        user_computer_numbers.append(number_user)
    return number_user, user_computer_numbers


#-------------------------------------------------------------computer------------------------------------------------------------
def get_number_computer(user_computer_numbers, feedback, ranges):
    """
    The function generates a random number for the computer.
    
    Args:
        user_computer_numbers (list): The list with the numbers entered by the user and the computer.
        feedback (str): The feedback given of validate number of computer.
        ranges (dict): A dictionary with the range of numbers to generate the random number.
        
    return:
        int: The number generated for the computer.

    """
    if not user_computer_numbers:
        return random.randint(ranges["min"], ranges["max"])

    last_number_user_computer = user_computer_numbers[-1]
    order_numbers_user_computer = sorted(set(user_computer_numbers))
    index = order_numbers_user_computer.index(last_number_user_computer)
    
    if feedback == "":
        return random.randint(ranges["min"], ranges["max"])
    if feedback == "El número es mayor.":
        if index == len(order_numbers_user_computer) - 1: # si el número es mayor que el último número de la lista
            return random.randint(order_numbers_user_computer[index], ranges["max"])
        else:
            return random.randint(order_numbers_user_computer[index], order_numbers_user_computer[index + 1])
    elif feedback == "El número es menor.":
        if index == 0:
            return random.randint(ranges["min"], order_numbers_user_computer[index])
        else:
            return random.randint(order_numbers_user_computer[index -1], order_numbers_user_computer[index])
    else:
        return random.randint(ranges["min"], ranges["max"])


def set_number_computer(user_computer_numbers, feedback, ranges):
    """
    This function call the get_number_computer function and add the number entered by the computer to a list.
    
    Args:
        user_computer_numbers (list): The list with the numbers entered by the user and the computer.
        feedback (str): The feedback given of validate number of computer.
        ranges (dict): A dictionary with the range of numbers to generate the random number.
        
    Return:
        int: The number entered by the computer.
        list: The list update with the number entered by the user and the computer.
        
    """
    number_computer = get_number_computer(user_computer_numbers, feedback, ranges)
    user_computer_numbers.append(number_computer)
    return number_computer, user_computer_numbers


def print_number_user_computer(number_user, number_computer):
    """
    The function prints the number entered by the user and the computer.
    """
    print("El usuario ha introducido el número: ", number_user)
    print("El ordenador ha introducido el número: ", number_computer)
    
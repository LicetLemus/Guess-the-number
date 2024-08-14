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


def validate_number_user(input_value):
    if input_value.isdigit() and int(input_value) > 0:
        return int(input_value)
    else:
        print("No has introducido un numero válido")
        return None # si no es un número válido, devolvemos None

def set_number_user(user_computer_numbers):
    """
    This function call the validate_number_user function and add the number entered by the user to a list.
    
    Args:
        None
        
    Return:
        list: The list with the number entered by the user.
    """
    input_value = get_input_value()
    number_user = validate_number_user(input_value)
    if number_user is not None:
        user_computer_numbers.append(number_user)
    return number_user, user_computer_numbers

#-------------------------------------------------------------computer------------------------------------------------------------
def get_number_computer(user_computer_numbers, feedback, ranges):
    """
    The function generates a random number for the computer.
    
    Args:
        number_user (int): The number entered by the user.
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
        return random.randint(order_numbers_user_computer[index], order_numbers_user_computer[index + 1])
    elif feedback == "El número es menor.":
        return random.randint(order_numbers_user_computer[index -1], order_numbers_user_computer[index])
    else:
        return random.randint(ranges["min"], ranges["max"])


def set_number_computer(user_computer_numbers, feedback, ranges):
    """
    This function call the get_number_computer function and add the number entered by the computer to a list.
    
    Args:
        number_user (int): The number entered by the user.
        
    Return:
        list: The list with the number entered by the computer.
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
    
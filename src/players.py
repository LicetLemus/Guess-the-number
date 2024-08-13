import random

list_number_user = []
list_number_computer = []

def get_number_user():
    """The function allows the user to enter a number"""
    return int(input("\nIntroduce un número: "))


def set_number_user():
    """
    This function allows add the number entered by the user to a list.
    
    Args:
        None
        
    Return:
        list: The list with the number entered by the user.
    """
    number_user_current = get_number_user()
    list_number_user.append(number_user_current)
    return list_number_user
    

def get_number_computer(number_user):
    """The function allows the computer to enter a number"""
    number_computer = 0
    
    if number_user >= 50:
        number_computer = random.randint(50, number_user - 1)
        return number_computer
    else:
        number_computer = random.randint(number_user + 1, 49)
        return number_computer

    
def set_number_computer(number_user):
    """
    This function allows add the number entered by the computer to a list.
    
    Args:
        None
        
    Return:
        list: The list with the number entered by the computer.
    """
    number_computer_current = get_number_computer(number_user)
    list_number_computer.append(number_computer_current)
    return list_number_computer

def print_number_user_computer(number_user, number_computer):
    print("El usuario ha introducido el número: ", number_user[-1])
    print("El ordenador ha introducido el número: ", number_computer[-1])
    
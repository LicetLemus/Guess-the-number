import random

def get_number_user():
    """The function allows the user to enter a number"""
    number_user = []
    number_user.append(int(input("\nIntroduce un número: ")))
    return number_user

def get_number_computer(number_user, number_random):
    """The function allows the computer to enter a number"""
    number_computer = []
    
    if number_user[-1] > number_random:
        number_computer.append(random.randint(1, number_user[-1] - 1))
        return number_computer
    else:
        number_computer.append(random.randint(number_user[-1] + 1, 100))
        return number_computer
    

def print_number_user_computer(number_user, number_computer):
    print("El usuario ha introducido el número: ", number_user[-1])
    print("El ordenador ha introducido el número: ", number_computer[-1])
    
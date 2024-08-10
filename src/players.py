import random

number_user = []
number_computer = []

def player_user():
    """The function allows the user to enter a number"""

    number_user.append(int(input("\nIntroduce un número: ")))


def player_computer(number_random):
    """The function allows the computer to enter a number"""

    if number_user[-1] > number_random:
        number_computer.append(random.randint(1, number_user[-1] - 1))
    else:
        number_computer.append(random.randint(number_user[-1] + 1, 100))
    print("El ordenador ha elegido el numero: ", number_computer[-1])
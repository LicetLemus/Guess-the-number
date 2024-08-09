"""
randint return a random number selected element from the specified range
random.randint(start, end)
start Required. An integer specific at which position to start.
end Required. An integer specific at which position to end.

"""

import random

number_user = []
number_computer = []
MAX_TRY = 10

def validate_number(number, number_random):
    """The function validates the number entered by the user
    and compares it with the random number"""

    if number == number_random:
        print("¡Felicidades! Has adivinado el número")
    if number < number_random:
        print("El número a adivinar es mayor")
    else:
        print("El número a adivinar es menor")

def player_user():
    """The function allows the user to enter a number"""

    number_user.append(int(input("\nIntroduce un número: ")))